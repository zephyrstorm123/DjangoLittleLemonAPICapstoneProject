from rest_framework import serializers
from .models import Booking, Menu

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'name', 'number_of_guests', 'Booking_date')
        extra_kwargs = {
            'name': {'required': True},
            'number_of_guests': {
                'required': True,
                'min_value': 1,
                'max_value': 1000,
                },
            'Booking_date': {'required': True},
        }

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'price', 'inventory')
        extra_kwargs = {
            'name': {'required': True},
            'price': {
                'required': True,
                'min_value': 1,
                },
            'inventory': {
                'required': True,
                'min_value': 0
                },
        }