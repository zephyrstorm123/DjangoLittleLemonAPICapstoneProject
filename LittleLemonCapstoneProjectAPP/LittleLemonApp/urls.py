from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('index', views.index, name='index'),
    path('menu', views.MenuItemsView.as_view({'get': 'list'}), name='menu'),
    path('menu/<int:pk>', views.SingleItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='menu'),
    path('api-auth-token', obtain_auth_token),
    path('booking', views.BookingView.as_view({'get': 'list', 'post': 'create'}), name='booking'),
    path('booking/<int:pk>', views.BookingItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking'),
]