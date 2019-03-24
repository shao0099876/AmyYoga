from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from .forms import ChangePasswordForm, ForgetPasswordForm, UsernameForm
from UserLogin.models import Customer as UserDB
from UserLogin.models import SecurityQA as SecurityQADB


# Create your views here.
def changePassword(request):
    if request.session.get('authority', default=None) == 'Administrator':
        return HttpResponse("管理员禁止使用修改密码功能")
    if request.method == 'POST':
        username = request.session.get('username', default=None)
        if username is None:
            return HttpResponsePermanentRedirect('/')
        changePasswordForm = ChangePasswordForm(request.POST)
        if changePasswordForm.is_valid():
            oldPassword = changePasswordForm.cleaned_data['oldPassword']
            user = UserDB.objects.get(username=username)
            if user.checkAuthority(oldPassword):
                newPassword = changePasswordForm.cleaned_data['newPassword']
                confirmPassword = changePasswordForm.cleaned_data['confirmPassword']
                if newPassword == confirmPassword:
                    user.setPassword(newPassword)
                    return HttpResponse("修改成功")
                else:
                    errormessage = "两次密码不匹配"
            else:
                errormessage = "旧密码不正确"
    else:
        changePasswordForm = ChangePasswordForm()
    return render(request, "ChangePasswordUI.html", locals())


def forgetPassword(request):
    if request.session.get('authority', default=None) == 'Administrator':
        return HttpResponse("管理员禁止使用修改密码功能")
    if request.method == 'POST':

    else:
        if request.session.get('username', default=None) is None:
            usernameForm = UsernameForm()
    return render(request, 'ChangePasswordUI.html', locals())

def forgetPasswordLogin(request):
    if request.method=='POST':
        usernameForm=UsernameForm(request.POST)
        if usernameForm.is_valid():
            username=usernameForm.cleaned_data['username']
            user=UserDB.objects.get(username=username,default=None)
            if user is None:
                errormessage="此用户名不存在"
            else:
                request.session['username']=username
                usernameForm=None
    return render(request,'changePasswordUI.html',locals())