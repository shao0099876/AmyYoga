from django.urls import path
from .views import *

urlpatterns = {
    path('yoga/', yogamessage),
    path('teacherteam/', teacherteam),
    path('location/', location),
    path('course/', course),
}
