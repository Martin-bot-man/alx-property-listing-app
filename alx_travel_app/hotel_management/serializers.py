from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    """
    Main serializer for the Listing model.
    """
    
    # Display readable property type
    property_type_display = serializers.CharField(
        source='get_property_type_display', 
        read_only=True
    )
    
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'property_type',
            'property_type_display',
            'price_per_night',
            'location',
            'max_guests',
            'amenities'
        ]
        read_only_fields = ['id']
    
    def validate_price_per_night(self, value):
        """Validate that price per night is positive."""
        if value <= 0:
            raise serializers.ValidationError(
                "Price per night must be greater than 0."
            )
        return value
    
    def validate_max_guests(self, value):
        """Validate that max_guests is at least 1."""
        if value < 1:
            raise serializers.ValidationError(
                "Maximum guests must be at least 1."
            )
        return value
    
    def validate_amenities(self, value):
        """Validate that amenities is a list."""
        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Amenities must be a list."
            )
        return value