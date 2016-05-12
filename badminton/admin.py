from django.contrib import admin

from .models import Player


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'nfc_id')

admin.site.register(Player, UserAdmin)
