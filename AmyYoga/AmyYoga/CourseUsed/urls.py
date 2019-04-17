from django.urls import path
from . import views
urlpatterns = {
    path('', views.CourseUsed),
    path('<record_id>',views.moremessage),
}