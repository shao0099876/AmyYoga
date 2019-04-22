from django.urls import path, include
from .views import *

'''
第三次迭代重要计划：
视图函数复用，HTML文件复用，使用模板嵌入式代码对用户身份进行判断，以确定显示内容
合并计划：modifyCourse，viewCourse，deletecourse，readdcourse合并为同一个视图函数

'''
modifypatterns = {
    path('', modifyCourse),
    path('<coursename>/', ModCourse),
}
deletepatterns = {
    path('', deletecourse),
    path('<coursename>/', DelCourse),
}
restorepatterns = {
    path('', readdcourse),
    path('<coursename>/', reAddCourse),
}
viewpatterns={
    path('',viewCourse),
    path('<coursename>/',viewCourseDetails),
}
urlpatterns = {
    path('view/',include(viewpatterns)),
    path('add/', addCourse),
    path('modify/', include(modifypatterns)),
    path('delete/', include(deletepatterns)),
    path('restore/', include(restorepatterns)),
}
