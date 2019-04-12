from django.urls import path
from . import  views
urlpatterns = {
    path('', views.admin_coursemessage),#显示查看课程界面，初始界面
    path('<coursename>', views.Coursename)
}