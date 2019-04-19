from django.urls import path
from . import views
urlpatterns = {
    path('', views.CourseUsed),
    path('<username>',views.moremessage_username),
    path('<coursename>',views.moremessage_coursename),
}