from django.urls import path,include
from .views import *
adminurlpatterns = {
    path('', superusermessage),
    path('<user>/', moremessage),
}
urlpatterns = {
    path('customer/', customerCompleteInformation),
    path('admin/',include(adminurlpatterns)),
}