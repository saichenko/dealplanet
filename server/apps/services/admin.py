from django.contrib import admin

from apps.services.models.addresses import Address
from apps.services.models.categories import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_default')
    search_fields = ('name', 'city', 'state', 'street')
    readonly_fields = ('longitude', 'latitude')
