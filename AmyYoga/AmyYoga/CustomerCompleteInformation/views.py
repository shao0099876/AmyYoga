from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import CompleteForm
from UserLogin.models import PersonalInformation as PersonalInformationDB
from Tools import SessionManager,FormsManager

# Create your views here.
def completeinformation(request):#用户点击提交完善的个人信息
    if request.method == 'POST':  # 如果请求为表单提交
        completeForm = CompleteForm(request.POST)  # 获取表单内容
        if completeForm.is_valid():  # 解析表单
            name=FormsManager.getdata(completeForm,'name')
            age=FormsManager.getdata(completeForm,'age')
            profession=FormsManager.getdata(completeForm,'profession')
            phoneNumber=FormsManager.getdata(completeForm,'phoneNumber')
            sex=FormsManager.getdata(completeForm,'sex')
            birthday=FormsManager.getdata(completeForm,'birthday')
            height=FormsManager.getdata(completeForm,'height')
            weight=FormsManager.getdata(completeForm,'weight')
            bust=FormsManager.getdata(completeForm,'bust')
            waistline=FormsManager.getdata(completeForm,'waistline')
            hipline=FormsManager.getdata(completeForm,'hipline')
            shoulderwidth=FormsManager.getdata(completeForm,'shoulderwidth')

            #判断数据是否正确

            #正确过后写数据库
            username=SessionManager.getUsername(request)
            personalInformation = PersonalInformationDB.objects.get(username=username)

            personalInformation.setName(name)
            personalInformation.setAge(age)
            personalInformation.setProfession(profession)
            personalInformation.setPhoneNumber(phoneNumber)
            personalInformation.setSex(sex)
            personalInformation.setBirthday(birthday)
            personalInformation.setHeight(height)
            personalInformation.setWeight(weight)
            personalInformation.setBust(bust)
            personalInformation.setWaistline(waistline)
            personalInformation.setHipline(hipline)
            personalInformation.setShoulderwidth(shoulderwidth)

            return HttpResponseRedirect("/customerloginedindex/")  # 跳转登陆后首页

    else:
        completeForm = CompleteForm()  # 创建表单
    return render(request, 'completeinformationUI.html', locals())  # 渲染页面
