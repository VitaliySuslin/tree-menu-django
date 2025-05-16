from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название пункта')
    url = models.CharField(max_length=255, verbose_name='URL', blank=True, null=True)
    named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=100, verbose_name='Название меню')

    def __str__(self):
        return self.name

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        return '#'