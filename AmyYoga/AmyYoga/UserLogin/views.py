from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from Tools.SessionManager import SessionManager
from .forms import LoginForm
from Database.models import Customer


# Create your views here.
def login(request):  # 用户登录功能视图函数
    sessionManager = SessionManager(request)
    if request.method == 'POST':  # 如果请求为表单提交
        loginForm = LoginForm(request.POST)  # 获取表单内容
        if loginForm.is_valid():  # 解析表单
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            user = Customer.objects.get(username=username)  # 尝试查询该用户
            sessionManager.setLogin(username)
            if sessionManager.isAdministrator():
                return HttpResponseRedirect("/administratorloginedindex/")
            else:
                return HttpResponseRedirect("/customerloginedindex/")
    else:  # 如果是普通访问（GET方法）
        if sessionManager.isLogined():
            return HttpResponseRedirect('/')  # 如果已经登录，跳转到首页
        else:
            loginForm = LoginForm()  # 创建表单
    return render(request, 'loginUI.html', locals())  # 渲染页面


def logout(request):
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():
        sessionManager.setLogout()
    return HttpResponseRedirect("/")
