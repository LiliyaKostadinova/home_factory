from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ListingForm
from .models import Listing

def listings(request):
    listings = Listing.objects.all().filter(is_published=True)
    context = {'listings': listings}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.all().order_by('-list_date')
    
    # Search by Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # Search by City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)
            
    # Search by street / district
    if 'street_address' in request.GET:
        street_address = request.GET['street_address']
        if street_address:
            queryset_list = queryset_list.filter(street_address__icontains=street_address)
            
    # Search by number of rooms
    if 'number_of_rooms' in request.GET:
        number_of_rooms = request.GET['number_of_rooms']
        if number_of_rooms:
            queryset_list = queryset_list.filter(number_of_rooms__iexact=number_of_rooms)
    
    # Search by maximum price
    if 'max_price' in request.GET:
        price = request.GET['max_price']
        if price:
            try:
                price_float = float(price)
                queryset_list = queryset_list.filter(price__lte=price_float)
            except:
                queryset_list = Listing.objects.all().order_by('-list_date')
    
    context = {
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect('dashboard')
    else:
        form = ListingForm()
    return render(request, 'listings/create_listing.html', {'form': form})
