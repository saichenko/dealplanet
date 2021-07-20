import django_filters

from .models.offers import Offer


class OfferFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Offer
        fields = ['category', 'name']
