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
from CustomerRegister import views as CustomerRegisterView
from CustomerCompleteInformation import views as CustomerCompleteInformationView

from ChangePassword import views as ChangePasswordView
from Index import views as IndexView
from django.views import static
from CustomerCourse import views as CustomerCourseView
from admin_CourseMessage import views as admin_CourseMessageView

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    path('login/', include('UserLogin.urls')),
    path('register/',include('CustomerRegister.urls')),
    path('',include('Index.urls')),
    path('PersonalInformation/',include('PersonalInformation.urls')),
    path('password/',include('ChangePassword.urls')),
    path('course/',include('Course.urls')),
]
