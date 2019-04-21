from django.urls import path
from . import  views
urlpatterns = {
    path('', views.buycourse),
    path('<user_name>/<course_name>', views.makebuycourse),
}