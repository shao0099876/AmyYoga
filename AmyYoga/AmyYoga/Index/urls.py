from django.urls import path
from .views import *

urlpatterns = {
    path('', index),
    path('teacherteam/',teacherteam),
    path('yogamessage/',yogamessage),
    path('aboutlocation/',aboutlocation),
    path('aboutclass/',aboutclass),
    path('customer/',customerloginedindex),
    path('administrator/',administratorloginedindex),
}
