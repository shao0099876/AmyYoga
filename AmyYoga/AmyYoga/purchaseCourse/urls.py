from django.urls import path
from . import  views
urlpatterns = {
    path('', views.purchaseCourse, name='temp'),
    path('<course>', views.purchase, ),
}