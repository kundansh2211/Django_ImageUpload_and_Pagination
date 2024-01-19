from django.urls import path
from .views import add_hotel, show_hotels

urlpatterns = [
    path('add_hotel/', add_hotel),
    path('show_hotels/', show_hotels, name='show_url')
]
