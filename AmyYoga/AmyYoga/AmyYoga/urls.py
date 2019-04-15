"""AmyYoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from UserLogin import views as UserLoginView
from CustomerRegister import views as CustomerRegisterView
from CustomerCompleteInformation import views as CustomerCompleteInformationView
from CourseUsed import views as CourseUsedView

from ChangePassword import views as ChangePasswordView
from Index import views as IndexView
from django.views import static
from CustomerCourse import views as CustomerCourseView
from admin_CourseMessage import views as admin_CourseMessageView

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.login),  # 导向用户登录功能的URL
    path('register/', CustomerRegisterView.register),
    path('', IndexView.index),  # 首页URL
    path('logout/',UserLoginView.logout),
    path('completeinformation/',CustomerCompleteInformationView.completeinformation),#用户完善个人信息
    path('forgetpassword/',ChangePasswordView.forgetPassword),
    path('changepassword/',ChangePasswordView.changePassword),#自己起的名字，app名View，view中的函数名
    path('forgetpasswordlogin/',ChangePasswordView.forgetPasswordLogin),
    path('courseused/',CourseUsedView.CourseUsed),
    path('superusermessage/', include('superuser_message.urls')),#管理员查看会员信息

    path('teacherteam/', IndexView.teacherteam),  # 首页中的课程相关界面
    path('yogamessage/', IndexView.yogamessage),  # 首页中的瑜伽科普界面
    path('aboutlocation/', IndexView.aboutlocation),  # 首页中的场地相关界面
    path('aboutclass/', IndexView.aboutclass),  # 首页中的课程相关界面
    path('customerloginedindex/',IndexView.customerloginedindex), #客户登陆过后显示的首界面
    path('administratorloginedindex/', IndexView.administratorloginedindex),  # 管理员登陆过后显示的首界面
    url('^static/(?P<path>.*)$',static.serve,{'document_root':settings.STATIC_ROOT},name='static'),

    path('customercourse/',CustomerCourseView.customercourse), #客户登陆中的我的课程中的已支付界面（默认界面）
    path('uncustomercourse/',include('CustomerCourse.urls')), #客户登陆中的我的课程中的未支付界面

    path('admin_coursemessage/',include('admin_CourseMessage.coursemessageurls')),#管理员登陆状态下查看课程信息
    path('addcourse/',admin_CourseMessageView.addcourse),#管理员登陆状态下增加课程信息
    path('modifycourse/',include('admin_CourseMessage.modifycourseurls')),#管理员登陆状态下修改课程信息
    path('deletecourse/',include('admin_CourseMessage.deletecourseurls')),#管理员登陆状态下下架课程信息
    path('readdcourse/',include('admin_CourseMessage.readdcourseurls')),#管理员登陆状态下重新上架课程信息
]
