from django.urls import path

from . import views

urlpatterns = [
    path('', views.forgetPassword),
    path('forgetpasswordlogin/',views.forgetPasswordLogin)
]