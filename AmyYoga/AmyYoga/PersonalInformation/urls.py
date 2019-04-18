from django.urls import path, include
from .views import *

adminurlpatterns = {
    path('', adminViewInformation),
    path('<username>/', adminViewDetails),
}
urlpatterns = {
    path('customer/', customerCompleteInformation),
    path('admin/', include(adminurlpatterns)),
}
