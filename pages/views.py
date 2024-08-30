from django.shortcuts import render
from listings.models import Listing

def index(request):
    listings = Listing.objects.all().filter(is_published=True)[:6]
    context = {'listings': listings}
    return render(request, 'pages/index.html', context)

def statistics(request):
    return render(request, 'pages/statistics.html')
