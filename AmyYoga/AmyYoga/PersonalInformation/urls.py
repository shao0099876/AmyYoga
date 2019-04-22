from django.urls import path, include
from .views import *

adminurlpatterns = {
    path('', viewMemeberList),
    path('<username>/', viewDetails),
}
urlpatterns = {
    path('customer/', customerCompleteInformation),
    path('admin/', include(adminurlpatterns)),
}
