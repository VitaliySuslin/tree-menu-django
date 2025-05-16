from django import template
from django.urls import resolve
from ..models import MenuItem


register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = resolve(request.path_info).url_name
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    
    def build_menu(items, parent=None):
        menu = []
        for item in items:
            if item.parent == parent:
                children = build_menu(items, item)
                menu.append({
                    'item': item,
                    'children': children,
                    'is_active': item.named_url == current_url or item.url == request.path
                })
        return menu

    menu = build_menu(menu_items)
    return {'menu': menu}