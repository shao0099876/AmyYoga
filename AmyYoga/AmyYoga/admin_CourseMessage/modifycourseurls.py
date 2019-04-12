from django.urls import path
from . import  views
urlpatterns = {
    path('', views.modifycourse),#显示修改课程界面
    path('<coursename>', views.ModCourse)
}