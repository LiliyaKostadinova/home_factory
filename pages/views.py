from django.shortcuts import render
from listings.models import Listing
from listings.search_choices import number_of_rooms_options, district_options

def index(request):
    listings = Listing.objects.all().filter(is_published=True)[:6]
    context = {
        'listings': listings,
        'number_of_rooms_options': number_of_rooms_options,
        'district_options': district_options
    }
    return render(request, 'pages/index.html', context)

def search(request):
    return render(request, 'listings/search.html')

def statistics(request):
    return render(request, 'pages/statistics.html')
