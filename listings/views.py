from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ListingForm

def listings(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

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
