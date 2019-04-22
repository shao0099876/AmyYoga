from django.urls import path
from .views import *

urlpatterns = {
    path('', index),
    path('customer/', customerIndex),
    path('administrator/', adminIndex),
}
