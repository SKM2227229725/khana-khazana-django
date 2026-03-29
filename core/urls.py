
from django.urls import path
from core.views import home ,menu, contact, tracking, reservation

urlpatterns = [
    path( '', home, name='home' ),
    path( 'menu/', menu, name='menu' ),
    path( 'track/', tracking, name='track' ),
    path( 'reservation/', reservation, name='reservation' ),
    path( 'contact/', contact, name='contact' ),
]
