from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.users import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_filter = ('email', 'date_joined')
    readonly_fields = ('id', 'date_joined', 'last_login')
    search_fields = ('email',)
    list_display = ('email', 'date_joined', 'last_login',
                    'is_admin', 'is_staff')

    ordering = ('id',)
    filter_horizontal = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
