from django.urls import path, include
from .views import *

forgetpatterns = {
    path('', forgetPassword),
    path('login/', forgetPasswordLogin),
}
urlpatterns = {
    path('forget/', include(forgetpatterns)),
    path('change/', changePassword),
}
