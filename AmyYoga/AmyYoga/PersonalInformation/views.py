from django.shortcuts import render, HttpResponseRedirect
from .forms import CompleteForm
from Database.models import PersonalInformation as PersonalInformationDB
from Tools import SessionManager


# Create your views here.
def customerCompleteInformation(request):  # 用户点击提交完善的个人信息
    if request.method == 'POST':  # 如果请求为表单提交
        completeForm = CompleteForm(request.POST)  # 获取表单内容
        if completeForm.is_valid():  # 解析表单
            name = completeForm.cleaned_data.get('name')
            age = completeForm.cleaned_data.get('age')
            profession = completeForm.cleaned_data.get('profession')
            phoneNumber = completeForm.cleaned_data.get('phoneNumber')
            sex = completeForm.cleaned_data.get('sex')
            birthday = completeForm.cleaned_data.get('birthday')
            height = completeForm.cleaned_data.get('height')
            weigt = completeForm.cleaned_data.get('weight')
            bust = completeForm.cleaned_data.get('bust')
            waistline = completeForm.cleaned_data.get('waistline')
            hipline = completeForm.cleaned_data.get('hipline')
            shoulderwidth = completeForm.cleaned_data.get('shoulderwidth')

            # 判断数据是否正确

            # 正确过后写数据库
            username = SessionManager.getUsername(request)
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
        usernamedd = SessionManager.getUsername(request)
        userid = PersonalInformationDB.objects.filter(username=usernamedd)
        if userid:
            completeForm = CompleteForm(instance=userid[0])
        else:
            completeForm = CompleteForm()  # 创建表单
    return render(request, 'completeinformationUI.html', locals())  # 渲染页面


def superusermessage(request):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    user_list = PersonalInformationDB.objects.all()
    return render(request, 'vipmessage.html', locals())


def moremessage(request, user):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    user_list = PersonalInformationDB.objects.filter(username=user)
    # return HttpResponse(user)
    return render(request, 'moremessage.html', locals())
