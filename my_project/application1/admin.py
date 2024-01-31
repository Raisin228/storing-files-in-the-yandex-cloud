from django.contrib import admin
from .models import AnyFile


class AnyFileDisplayOnAdminPanel(admin.ModelAdmin):
    """Форма для админ панели"""
    list_display = ['some_name', 'image', 'file']


admin.site.register(AnyFile, AnyFileDisplayOnAdminPanel)
