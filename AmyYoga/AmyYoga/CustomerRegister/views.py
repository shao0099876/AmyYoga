from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm
from UserLogin.models import Customer as CustomerDB


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # 获取表单内容
        if form.is_valid():  # 解析表单
            username = form.cleaned_data['username']  # 获得表单内用户名
            password = form.cleaned_data['password']  # 获得表单内密码
            confirmPassword = form.cleaned_data['confirmPassword']
            phoneNumber = form.cleaned_data['phoneNumber']
            if confirmPassword != password:
                return HttpResponse("两次密码不一致")
            user = CustomerDB()  # 创建空用户对象
            try:
                user = CustomerDB.objects.get(username=username)  # 尝试查询该用户
            except ObjectDoesNotExist:
                user.username = username
                user.password = password
                user.createPersonalInformation(phoneNumber)
                user.save()
                return HttpResponse(
                    user.username + " " + user.password + " " + user.personalInformation.phoneNumber)  # 如果没查询到，返回可以注册信息
            return HttpResponse("用户名已存在，不可注册")  # 返回用户名存在，不可注册信息
    else:
        form = RegisterForm()
        return render(request, "registerUI.html", {"registerForm": form})
