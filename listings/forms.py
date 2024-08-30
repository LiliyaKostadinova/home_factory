from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'type',
            'is_published',
            'street_address',
            'city',
            'price',
            'lot_size',
            'story',
            'number_of_rooms',
            'bathrooms',
            'building_year',
            'description',
            'required_commission',
            'photo_main',
            'list_date'
        ]