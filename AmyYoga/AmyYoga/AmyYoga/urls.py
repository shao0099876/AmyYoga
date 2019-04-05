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
from CustomerBuyCourse import views as CustomerBuyCourseView

from ChangePassword import views as ChangePasswordView
from Index import views as IndexView
from django.views import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.login),  # 导向用户登录功能的URL
    path('register/', CustomerRegisterView.register),
    path('', CustomerBuyCourseView.customerbuycourse),  # 首页URL
    path('logout/',UserLoginView.logout),
    path('completeinformation/',CustomerCompleteInformationView.completeinformation),#用户完善个人信息
    path('forgetpassword/',ChangePasswordView.forgetPassword),
    path('changepassword/',ChangePasswordView.changePassword),#自己起的名字，app名View，view中的函数名
    path('forgetpasswordlogin/',ChangePasswordView.forgetPasswordLogin),
    path('superusermessage/', include('superuser_message.urls')),#管理员查看会员信息

    path('teacherteam/', IndexView.teacherteam),  # 首页中的课程相关界面
    path('yogamessage/', IndexView.yogamessage),  # 首页中的瑜伽科普界面
    path('aboutlocation/', IndexView.aboutlocation),  # 首页中的场地相关界面
    path('aboutclass/', IndexView.aboutclass),  # 首页中的课程相关界面
    path('customerloginedindex/',IndexView.customerloginedindex), #客户登陆过后显示的首界面
    path('administratorloginedindex/', IndexView.administratorloginedindex),  # 管理员登陆过后显示的首界面
    url('^static/(?P<path>.*)$',static.serve,{'document_root':settings.STATIC_ROOT},name='static'),
    path('customerbuycourse/', CustomerBuyCourseView.customerbuycourse),  # 用户购买课程
]
