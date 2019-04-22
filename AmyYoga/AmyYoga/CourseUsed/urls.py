from django.urls import path
from .views import *
viewpatterns={
    #path('',CourseUsed),
    #path('',UserCourseUsed),
    #这条要改
    #path('user/<username>/',moremessage_username),
    #path('course/<coursename>/',moremessage_coursename),
}
urlpatterns = {
    # path('view/', viewpatterns),
    # path('new/',viewpatterns),
    #这条新加的，给销课功能留的URL，把CourseUsed功能中的销课逻辑拿出来放进单独的视图函数并关联到这个URL
}