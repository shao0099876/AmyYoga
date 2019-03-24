from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render

from Tools import FormsManager,SessionManager

from .forms import LoginForm
from .models import Customer as UserDB


# Create your views here.
def login(request):  # 用户登录功能视图函数
    if request.method == 'POST':  # 如果请求为表单提交
        loginForm = LoginForm(request.POST)  # 获取表单内容
        if loginForm.is_valid():  # 解析表单
            username=FormsManager.getData(loginForm,'username')
            password=FormsManager.getData(loginForm,'password')
            user = UserDB()  # 创建空用户对象
            try:
                user = UserDB.objects.get(username=username)  # 尝试查询该用户
            except ObjectDoesNotExist:
                errormessage = "UsernameDoesNotExist"  # 如果没查询到，返回用户名不存在信息
                return render(request, 'loginUI.html', locals())
            if user.checkAuthority(password):  # 如果认证成功
                SessionManager.setLogin(request,username,user.isAdministrator())
                return HttpResponse("Logined")
            else:
                errormessage = "PasswordWrong"  # 返回密码错误信息
    else:  # 如果是普通访问（GET方法）
        if SessionManager.isLogined(request):
            return HttpResponsePermanentRedirect('/')  # 如果已经登录，跳转到首页
        else:
            loginForm = LoginForm()  # 创建表单
    return render(request, 'loginUI.html', locals())  # 渲染页面


def logout(request):
    if SessionManager.isLogined(request):
        SessionManager.setLogout(request)
        return HttpResponse('logout')
    else:
        return HttpResponsePermanentRedirect("/")
