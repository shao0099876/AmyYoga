from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import ChangePasswordForm, ForgetPasswordForm, UsernameForm
from UserLogin.models import Customer as UserDB
from Tools import SessionManager,FormsManager,Tools

# Create your views here.


def changePassword(request):
    if SessionManager.isAdministrator(request):
        return HttpResponse("管理员禁止使用修改密码功能") # 不修改
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/forgetpassword/")
    if request.method == 'POST':
        changePasswordForm = ChangePasswordForm(request.POST)
        if changePasswordForm.is_valid():
            oldPassword=FormsManager.getData(changePasswordForm,'oldPassword')
            username=SessionManager.getUsername(request)
            user = UserDB.objects.get(username=username)
            if user.checkAuthority(oldPassword):
                newPassword=FormsManager.getData(changePasswordForm,'newPassword')
                confirmPassword=FormsManager.getData(changePasswordForm,'confirmPassword')
                if newPassword == confirmPassword:
                    user.setPassword(newPassword)
                    return HttpResponseRedirect("/login/")#跳转登录页面
                else:
                    errormessage = "两次密码不匹配"
            else:
                errormessage = "旧密码不正确"
    else:
        changePasswordForm = ChangePasswordForm()
    return render(request, "ChangePasswordUI.html", locals())


def forgetPassword(request):
    if SessionManager.isAdministrator(request):
        return HttpResponse("管理员禁止使用修改密码功能")#不修改
    if SessionManager.getUsername(request) is None:
        return HttpResponseRedirect("/forgetpasswordlogin/")

    #如果method是post（发布
    if request.method == 'POST':
        forgetPasswordForm=ForgetPasswordForm(request.POST)
        #如果更改密码 有效
        if forgetPasswordForm.is_valid():
            username = SessionManager.getUsername(request)
            newPassword = FormsManager.getData(forgetPasswordForm, 'newPassword')
            confirmPassword = FormsManager.getData(forgetPasswordForm, 'confirmPassword')
            if newPassword == confirmPassword:
                user = UserDB.objects.get(username=username)
                user.setPassword(newPassword)
                return HttpResponse("修改成功")
            else:
                errormessage = "两次密码不匹配"
            #密保问题
    #如果不是发布而是请求

    else:
        forgetPasswordForm = ForgetPasswordForm()

    return render(request, 'forgetPasswordUI.html', locals())

def forgetPasswordLogin(request):
    if request.method=='POST':
        usernameForm=UsernameForm(request.POST)
        if usernameForm.is_valid():
            username=FormsManager.getData(usernameForm,'username')
            user=UserDB()
            try:
                user=UserDB.objects.get(username=username)
            except ObjectDoesNotExist:
                errormessage="此用户名不存在"
                return render(request,'forgetPasswordUI.html',locals())
            if user.isAdministrator():
                errormessage="管理员禁止使用此功能"
                return render(request,'forgetPasswordUI.html',locals())
            SessionManager.setUsername(request,username)
            return HttpResponseRedirect('/forgetpassword/')
    else:
        usernameForm=UsernameForm()
    return render(request,'forgetPasswordUI.html',locals())