from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

# Listing model 
class Listing(models.Model):
    '''Model class to describe the Listing object and its attributes.'''
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    TYPE_CHOICES = [
        ('for_rent', 'For Rent'),
        ('for_sale', 'For Sale'),
    ]
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    street_address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    lot_size = models.FloatField(max_length=100)
    story = models.IntegerField()
    number_of_rooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    building_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    required_commission = models.FloatField(max_length=100, default=0, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    photo_main = models.ImageField(
        upload_to='images/%Y/%m/%d/', 
        default='default_photos/default_no_photo.jpg'
    )
    
    # Select the field which will be displayed when looking for the object
    def __str__(self):
        return self.title 
    
    