from django.shortcuts import render
from .models import Listing
from rest_framework .decorators import action
from rest_framework.response import Response
from .serializers import ListingSerializer
from rest_framework import viewsets, permissions, status



# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    """ViewSet for Listing model providing CRUD operation.
    list:Get all Listings
    create: create a new Listing
    update: Update a Listing
    patrial_update: Partially update a Listing(PATCH)
    destroy: Delete a Listing"""