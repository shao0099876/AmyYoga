from django.urls import path
from .views import *

urlpatterns = {
    path('', index),
    path('customer/',customerloginedindex),
    path('administrator/',administratorloginedindex),
}
