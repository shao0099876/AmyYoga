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
from django.contrib import admin
from django.urls import path, include
from UserLogin import views as UserLoginView
from CustomerRegister import views as CustomerRegisterView
from ChangePassword import views as ChangePasswordView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.login),  # 导向用户登录功能的URL
    path('register/', CustomerRegisterView.register),
    path('', ChangePasswordView.changePassword),  # 首页URL，暂时导向用户登录，需要修改可修改
    path('logout/',UserLoginView.logout),
    path('forgetpassword/',ChangePasswordView.forgetPassword),
    path('changepassword/',ChangePasswordView.changePassword),
    path('forgetpasswordlogin/',ChangePasswordView.forgetPasswordLogin),
]