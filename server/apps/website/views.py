from django.shortcuts import render
from apps.services.methods import get_most_profitable_offers


def homepage(request):
    context = dict(
        offers=get_most_profitable_offers()
    )
    return render(request, 'homepage.html', context=context)
