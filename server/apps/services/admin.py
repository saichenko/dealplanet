from django.contrib import admin
from apps.services.models.addresses import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_default')
    search_fields = ('name', 'city', 'state', 'street')
    readonly_fields = ('longitude', 'latitude')
