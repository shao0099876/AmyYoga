from django.urls import path
from .views import *

urlpatterns = {
    path('yoga/', yoga),
    path('teacherteam/', teacherteam),
    path('location/', location),
    path('course/', course),
}
