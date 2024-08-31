from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Listing
from datetime import datetime

class ListingModelTests(TestCase):
    '''Test the Listing Model with some dummy data.'''
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='securepassword'
        )

        # Dummy listing
        self.listing = Listing.objects.create(
            owner=self.user,
            title='Dummy House',
            type='for sale',
            street_address='123 Ulitsa',
            city='Springfield',
            price=250000.00,
            lot_size=0.25,
            story=2,
            number_of_rooms=4,
            bathrooms=2.5,
            building_year=2000,
            description='A beautiful house in a great neighborhood.',
            required_commission=5000.00,
            list_date=datetime.now(),
            photo_main='images/sample.jpg'
        )

    def test_listing_creation(self):
        '''Test that the Listing instance was created correctly.'''
        self.assertEqual(self.listing.title, 'Dummy House')
        self.assertEqual(self.listing.type, 'for sale')
        self.assertEqual(self.listing.street_address, '123 Ulitsa')
        self.assertEqual(self.listing.price, 250000.00)
        self.assertEqual(self.listing.lot_size, 0.25)
        self.assertEqual(self.listing.story, 2)
        self.assertEqual(self.listing.number_of_rooms, 4)
        self.assertEqual(self.listing.bathrooms, 2.5)
        self.assertEqual(self.listing.building_year, 2000)
        self.assertEqual(self.listing.description, 'A beautiful house in a great neighborhood.')
        self.assertEqual(self.listing.required_commission, 5000.00)
        self.assertEqual(self.listing.photo_main, 'images/sample.jpg')
        self.assertTrue(self.listing.is_published)
        self.assertFalse(self.listing.is_featured)

    def test_listing_str(self):
        '''Test if the listing string method (representation) works as expected.'''
        self.assertEqual(str(self.listing), 'Dummy House')

    def test_listing_default_values(self):
        '''Test the default values for the Listing model.'''
        listing = Listing.objects.create(
            owner=self.user,
            title='Another House',
            type='for rent',
            street_address='Jolio 456',
            city='City1',
            price=150000.00,
            lot_size=0.30,
            story=1,
            number_of_rooms=3
        )
        self.assertFalse(listing.is_featured)
        self.assertEqual(listing.required_commission, 0)
        self.assertTrue(listing.is_published)

    def test_listing_photo_main_default(self):
        '''Test the default photo_main value.'''
        listing = Listing.objects.create(
            owner=self.user,
            title='No Photo House',
            type='for sale',
            street_address='444 Street',
            city='Varna',
            price=350000.00,
            lot_size=0.40,
            story=3,
            number_of_rooms=5
        )
        self.assertEqual(listing.photo_main, 'default_photos/default_no_photo.jpg')
