from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import ChangePasswordForm, ForgetPasswordForm, UsernameForm
from Database.models import Customer
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_index_logined, url_forget_password, url_login, url_forget_password_login, url_index


def changePassword(request):
    sessionManager = SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_index)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_admin)
    if request.method == 'POST':
        changePasswordForm = ChangePasswordForm(request.POST)
        changePasswordForm.username = sessionManager.getUsername()
        if changePasswordForm.is_valid():
            username = changePasswordForm.username
            user = Customer.objects.get(username=username)
            newPassword = changePasswordForm.cleaned_data.get('newPassword')
            user.setPassword(newPassword)
            sessionManager.setLogout()
            return HttpResponseRedirect(url_login)  # 跳转登录页面
    else:
        changePasswordForm = ChangePasswordForm()
    return render(request, "ChangePasswordUI.html", {'changePasswordForm': changePasswordForm})


def forgetPassword(request):
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():
        if sessionManager.isAdministrator():
            return HttpResponseRedirect(url_index_admin)
        return HttpResponseRedirect(url_index_customer)
    if sessionManager.getUsername() is None:
        return HttpResponseRedirect(url_forget_password_login)
    if request.method == 'POST':
        forgetPasswordForm = ForgetPasswordForm(request.POST)
        if forgetPasswordForm.is_valid():
            username = sessionManager.getUsername()
            newPassword = forgetPasswordForm.cleaned_data.get('newPassword')
            user = Customer.objects.get(username=username)
            user.setPassword(newPassword)
            return HttpResponseRedirect(url_login)
    else:
        forgetPasswordForm = ForgetPasswordForm()
    return render(request, 'forgetPasswordUI.html', {'forgetPasswordForm': forgetPasswordForm})


def forgetPasswordLogin(request):
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():
        if sessionManager.isAdministrator():
            return HttpResponseRedirect(url_index_admin)
        return HttpResponseRedirect(url_index_customer)
    if request.method == 'POST':
        usernameForm = UsernameForm(request.POST)
        if usernameForm.is_valid():
            username = usernameForm.cleaned_data.get('username')
            user = Customer.objects.get(username=username)
            if user.isAdministrator():
                return HttpResponseRedirect(url_index)
            sessionManager.setUsername(username)
            return HttpResponseRedirect(url_forget_password)
    else:
        usernameForm = UsernameForm()
    return render(request, 'forgetPasswordUI.html', {'usernameForm': usernameForm})
