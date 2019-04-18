from django.urls import path, include
from .views import *

forgetPasswordURLPatterns = {
    path('', forgetPassword),
    path('login/', forgetPasswordLogin),
}

urlpatterns = {
    path('forget/', include(forgetPasswordURLPatterns)),
    path('change/', changePassword),
}
