from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

# Generated URL patterns:
# GET    /listings/                     - List all listings
# POST   /listings/                     - Create a new listing
# GET    /listings/{id}/                - Retrieve a specific listing
# PUT    /listings/{id}/                - Update a listing (full)
# PATCH  /listings/{id}/                - Partial update
# DELETE /listings/{id}/                - Delete a listing
# GET    /listings/property_types/      - Get property types (custom)