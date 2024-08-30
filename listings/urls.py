from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('listing', views.listing, name='listing'),
    path('create_listing', views.create_listing, name='create_listing')
]