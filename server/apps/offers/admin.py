from django.contrib import admin

from .models.offer_images import OfferImage
from .models.offers import Offer


class OfferImageInline(admin.StackedInline):
    model = OfferImage


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'url')
    search_fields = ('name', 'description')
    list_filter = ('category',)

    inlines = [OfferImageInline]
