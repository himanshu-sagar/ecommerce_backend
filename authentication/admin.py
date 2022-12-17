from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'username')
        }),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
            )
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('email', 'password1', 'password2'),
    }), )
    list_display = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'username']
    search_fields = ('id', 'email', 'first_name', 'last_name', "username")
    ordering = ('id', )


admin.site.register(User, UserAdmin)