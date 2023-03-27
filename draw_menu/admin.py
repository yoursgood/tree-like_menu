from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_visible', 'order')
    list_editable = ('is_visible', 'order')
    list_filter = ('parent',)


admin.site.register(Menu)

