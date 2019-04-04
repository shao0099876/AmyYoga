from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from Database.models import Customer as CustomerDB
from Database.models import PersonalInformation as PersonalInformationDB
from Tools import SessionManager,FormsManager

# Create your views here.
def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)  # 获取表单内容
        if registerForm.is_valid():  # 解析表单
            username=FormsManager.getData(registerForm,'username')
            password=FormsManager.getData(registerForm,'password')
            confirmPassword=FormsManager.getData(registerForm,'confirmPassword')
            phoneNumber=FormsManager.getData(registerForm,'phoneNumber')
            birthday=FormsManager.getData(registerForm,'birthday')
            if confirmPassword != password:  # 检查两次密码是否一致
                errormessage="两次密码不一致"
                return render(request, "registerUI.html", locals())
            user = CustomerDB()  # 创建空用户对象
            try:
                user = CustomerDB.objects.get(username=username)  # 尝试查询该用户
            except ObjectDoesNotExist:  # 用户名不存在，执行创建操作
                CustomerDB.objects.create(username=username,password=password)
                personalInformation=PersonalInformationDB.objects.create(username=username)
                personalInformation.setPhoneNumber(phoneNumber)
                personalInformation.setBirthday(birthday)
                return HttpResponseRedirect("/login/")  # 跳转login
            errormessage="用户名已存在，不可注册"  # 返回用户名存在，不可注册信息
    else:
        registerForm = RegisterForm()
    return render(request, "registerUI.html", locals())  # 正常访问，渲染模板
