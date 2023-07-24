from django.shortcuts import render
from .models import Menu, Booking
from django.contrib.auth.models import User, Group
from .serializers import MenuSerializer, BookingSerializer
#DRF IMPORTS
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

# PAGINATION IMPORTS
from django.core.paginator import Paginator, EmptyPage

# AUTHENTICATION IMPORTS

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied

#THROTTLING IMPORTS
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import throttle_classes

#ERROR IMPORTS
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return render(request, 'index.html')

"""
Handles the Menu items

url = /restaurant/menu

GET - Returns a list of all menu items

url = restaurant/menu/<int:pk>

GET - Returns a single menu item
PUT - Updates a single menu item
DELETE - Deletes a single menu item
"""
class MenuItemsView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = [Paginator]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Menu.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)
    
class SingleItemView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def retrieve(self, request, pk=None):
        queryset = Menu.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = MenuSerializer(item)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        menu_item = Menu.objects.get(id=pk)
        serializer = MenuSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        menu_item = Menu.objects.get(id=pk)
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

"""
Handles the Bookings

url = /restaurant/booking
"""
class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookingItemView(viewsets.ViewSet):
    serializer_class = BookingSerializer

    def retrieve(self, request, pk=None):
        queryset = Booking.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = BookingSerializer(item)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        booking_item = Booking.objects.get(id=pk)
        serializer = BookingSerializer(booking_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        booking_item = Booking.objects.get(id=pk)
        booking_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)