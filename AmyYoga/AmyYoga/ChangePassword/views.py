from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect

from .forms import ChangePasswordForm, ForgetPasswordForm, UsernameForm
from Database.models import Customer as UserDB
from Tools import Tools
from Tools.SessionManager import SessionManager


# Create your views here.


def changePassword(request):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():
        return HttpResponse("管理员禁止使用修改密码功能")  # 不修改
    if sessionManager.isLogouted():
        return HttpResponseRedirect("/forgetpassword/")
    if request.method == 'POST':
        changePasswordForm = ChangePasswordForm(request.POST)
        changePasswordForm.username = sessionManager.getUsername()
        if changePasswordForm.is_valid():
            oldPassword=changePasswordForm.cleaned_data.get('oldPassword')
            username = changePasswordForm.username
            user = UserDB.objects.get(username=username)
            newPassword=changePasswordForm.cleaned_data.get('newPassword')
            user.setPassword(newPassword)
            sessionManager.setLogout()
            return HttpResponseRedirect("/login/")  # 跳转登录页面
    else:
        changePasswordForm = ChangePasswordForm()
    return render(request, "ChangePasswordUI.html", locals())


def forgetPassword(request):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():
        return HttpResponse("管理员禁止使用修改密码功能")  # 不修改
    if sessionManager.getUsername() is None:
        return HttpResponseRedirect("/forgetpasswordlogin/")
    # 如果method是post（发布
    if request.method == 'POST':
        forgetPasswordForm = ForgetPasswordForm(request.POST)
        # 如果更改密码 有效
        if forgetPasswordForm.is_valid():
            username = sessionManager.getUsername()
            newPassword=forgetPasswordForm.cleaned_data.get('newPassword')
            user = UserDB.objects.get(username=username)
            user.setPassword(newPassword)
            return HttpResponseRedirect("/login/")  # 跳转登录页面
    else:
        forgetPasswordForm = ForgetPasswordForm()

    return render(request, 'forgetPasswordUI.html', locals())


def forgetPasswordLogin(request):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():
        return HttpResponse("管理员禁止使用修改密码功能")  # 不修改
    if request.method == 'POST':
        usernameForm = UsernameForm(request.POST)
        if usernameForm.is_valid():
            username=usernameForm.cleaned_data.get('username')
            user = UserDB.objects.get(username=username)
            if user.isAdministrator():
                return HttpResponse("管理员禁止使用修改密码功能")
            sessionManager.setUsername(username)
            return HttpResponseRedirect('/forgetpassword/')
    else:
        usernameForm = UsernameForm()
    return render(request, 'forgetPasswordUI.html', locals())
