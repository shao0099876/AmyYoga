from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect

from Tools import FormsManager, SessionManager

from .forms import LoginForm
from Database.models import Customer


# Create your views here
def login(request):  # 用户登录功能视图函数
    if request.method == 'POST':  # 如果请求为表单提交
        loginForm = LoginForm(request.POST)  # 获取表单内容
        if loginForm.is_valid():  # 解析表单
            username = FormsManager.getData(loginForm, 'username')
            password = FormsManager.getData(loginForm, 'password')
            user = Customer.objects.get(username=username)  # 尝试查询该用户
            SessionManager.setLogin(request, username, user.isAdministrator())
            if SessionManager.isAdministrator(request):
                return HttpResponseRedirect("/administratorloginedindex/")
            else:
                return HttpResponseRedirect("/customerloginedindex/")
    else:  # 如果是普通访问（GET方法）
        if SessionManager.isLogined(request):
            return HttpResponseRedirect('/')  # 如果已经登录，跳转到首页
        else:
            loginForm = LoginForm()  # 创建表单
    return render(request, 'loginUI.html', locals())  # 渲染页面


def logout(request):
    if SessionManager.isLogined(request):
        SessionManager.setLogout(request)
    return HttpResponseRedirect("/")
