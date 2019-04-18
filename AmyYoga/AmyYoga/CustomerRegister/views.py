from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from Database.models import Customer as CustomerDB
from Database.models import PersonalInformation as PersonalInformationDB
from Tools.SessionManager import SessionManager
# Create your views here.
def register(request):
    sessionManager=SessionManager(request)
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)  # 获取表单内容
        if registerForm.is_valid():  # 解析表单
            username=registerForm.cleaned_data.get('username')
            password = registerForm.cleaned_data.get('password')
            confirmPassword = registerForm.cleaned_data.get('confirmPassword')
            phoneNumber=registerForm.cleaned_data.get('phoneNumber')
            birthday=registerForm.cleaned_data.get('birthday')
            user = CustomerDB()  # 创建空用户对象
            CustomerDB.objects.create(username=username,password=password)
            personalInformation=PersonalInformationDB.objects.create(username=username)
            personalInformation.setPhoneNumber(phoneNumber)
            personalInformation.setBirthday(birthday)
            return HttpResponseRedirect("/login/")  # 跳转login
    else:
        registerForm = RegisterForm()
    if sessionManager.isLogined():
        return HttpResponseRedirect("/")
    return render(request, "registerUI.html", locals())  # 正常访问，渲染模板
