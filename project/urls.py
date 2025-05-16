from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('main_menu/', TemplateView.as_view(template_name='menu/main_menu.html'), name='main_menu'),
]