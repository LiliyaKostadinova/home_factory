from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .search_choices import number_of_rooms_options, district_options
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
    
    context = {
        'number_of_rooms_options': number_of_rooms_options,
        'district_options': district_options,
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
