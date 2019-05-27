from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext

from .models import User


@admin.register(User)
class UserAdmin(DjAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'birthday')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email', 'birthday', 'language', 'picture',
            'address_line_1', 'address_line_2', 'phone', 'city', 'state', 'zip',
            'country', 'notes')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
