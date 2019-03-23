from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from .models import Customer as UserDB


# Create your views here.
def login(request):  # 用户登录功能视图函数
    if request.method == 'POST':  # 如果请求为表单提交
        loginForm = LoginForm(request.POST)  # 获取表单内容
        if loginForm.is_valid():  # 解析表单
            username = loginForm.cleaned_data['username']  # 获得表单内用户名
            password = loginForm.cleaned_data['password']  # 获得表单内密码
            user = UserDB()  # 创建空用户对象
            try:
                user = UserDB.objects.get(username=username)  # 尝试查询该用户
            except ObjectDoesNotExist:
                errormessage = "UsernameDoesNotExist"  # 如果没查询到，返回用户名不存在信息
                return render(request, 'loginUI.html', locals())
            if user.checkAuthority(password):  # 如果认证成功
                request.session['loginStatus'] = 'Online'  # 设置登录状态为在线
                if user.isAdministrator():  # 根据身份标志设置当前连接用户的权限标志
                    request.session['authority'] = 'Administrator'
                else:
                    request.session['authority'] = 'Customer'
                request.session['username'] = username
                return HttpResponse(  # 返回对应信息
                    "Logined,loginStatus=" + request.session.get("loginStatus") + " authority=" + request.session.get(
                        "authority"))
            else:
                errormessage = "PasswordWrong"  # 返回密码错误信息
    else:  # 如果是普通访问（GET方法）
        if request.session.get('loginStatus', default=None) is not None:  # 检查用户是否已经登录
            return HttpResponsePermanentRedirect('/')  # 如果已经登录，跳转到首页
        else:
            loginForm = LoginForm()  # 创建表单
    return render(request, 'loginUI.html', locals())  # 渲染页面


def logout(request):
    if request.session.get('loginStatus', default=None) is not None:
        del request.session['loginStatus']
        del request.session['authority']
        return HttpResponse('logout')
    else:
        return HttpResponsePermanentRedirect("/")
