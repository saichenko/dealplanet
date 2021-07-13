from django.db.models import QuerySet

from apps.offers.models.offers import Offer


def get_most_profitable_offers() -> QuerySet:
    """Return first 8 ordered QuerySet by discount."""
    offers = Offer.objects.order_by('discount')[:8]
    return offers
