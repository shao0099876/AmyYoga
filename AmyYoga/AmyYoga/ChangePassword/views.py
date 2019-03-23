from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from .forms import ChangePasswordForms
from UserLogin.models import Customer as UserDB

# Create your views here.
def changePassword(request):
    if request.session.get('authority',default=None)=='Administrator':
        return HttpResponse("管理员禁止使用修改密码功能")
    if request.method == 'POST':
        username=request.session.get('username',default=None)
        if username is None:
            return HttpResponsePermanentRedirect('/')
        changePasswordForm=ChangePasswordForms(request.POST)
        if changePasswordForm.is_valid():
            oldPassword=changePasswordForm.cleaned_data['oldPassword']
            user=UserDB.objects.get(username=username)
            if user.checkAuthority(oldPassword):
                newPassword=changePasswordForm.cleaned_data['newPassword']
                confirmPassword=changePasswordForm.cleaned_data['confirmPassword']
                if newPassword==confirmPassword:
                    user.setPassword(newPassword)
                    return HttpResponse("修改成功")
                else:
                    errormessage="两次密码不匹配"
            else:
                errormessage="旧密码不正确"
    else:
        changePasswordForm = ChangePasswordForms()
    return render(request, "ChangePasswordUI.html", locals())

def forgetPassword(request):
    if request.method=='POST':
        return HttpResponse("tmp")
    else:
