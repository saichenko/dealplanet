from django.contrib import admin

from .models.offers import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'url')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    list_display_links = ('name',)
