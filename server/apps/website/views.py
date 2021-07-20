from django_filters.views import FilterView

from apps.offers.filters import OfferFilterSet
from apps.offers.models.offers import Offer
from apps.services.methods import get_most_popular_categories


class Homepage(FilterView):
    model = Offer
    context_object_name = 'offers'
    template_name = 'homepage.html'
    filterset_class = OfferFilterSet

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = get_most_popular_categories()

        current_cat = self.request.GET.get('category')
        data['current_cat'] = int(current_cat) if current_cat else None
        return data
