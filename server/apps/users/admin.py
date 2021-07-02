from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.users import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_filter = ('email', 'full_name', 'date_joined', 'is_teacher')
    readonly_fields = ('id', 'date_joined', 'last_login')
    search_fields = ('email', 'full_name')
    list_display = ('email', 'full_name', 'date_joined', 'last_login',
                    'is_admin', 'is_staff', 'is_teacher')

    ordering = ('id',)
    filter_horizontal = ()
    fieldsets = ()
