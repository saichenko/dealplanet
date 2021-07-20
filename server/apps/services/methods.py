from django.db.models import Count, QuerySet

from apps.services.models.categories import Category


def get_most_popular_categories() -> QuerySet:
    """Return QuerySet of first 8 most popular categories."""
    categories = Category.objects.annotate(
        offer_count=Count('offers')
    ).order_by('-offer_count')[:8]
    return categories
