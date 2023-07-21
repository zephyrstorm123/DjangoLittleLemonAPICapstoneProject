from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('menu', views.MenuItemsView.as_view({'get': 'list'}), name='menu'),
    path('menu/<int:pk>', views.SingleItemView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='menu'),
]