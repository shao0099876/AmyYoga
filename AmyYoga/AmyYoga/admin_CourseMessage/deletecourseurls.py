from django.urls import path
from . import  views
urlpatterns = {
    path('', views.deletecourse),#显示删除课程界面
    path('<coursename>', views.DelCourse)
}