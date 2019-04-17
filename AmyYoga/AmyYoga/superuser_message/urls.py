from django.urls import path
from . import  views
urlpatterns = {
    path('', views.superusermessage),
    path('<username>', views.moremessage)
}