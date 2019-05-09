from django.urls import path
from . import views
urlpatterns = {
    path('manager/', views.CourseUsed),
    path('user/',views.UserCourseUsed),
    #path('<username>',views.moremessage_username),
    #path('<coursename>',views.moremessage_coursename),
}