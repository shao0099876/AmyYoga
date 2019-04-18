from django.urls import path
from . import  views
urlpatterns = {
    path('', views.buycourse),
    path('makebuy/', views.makebuycourse),
}