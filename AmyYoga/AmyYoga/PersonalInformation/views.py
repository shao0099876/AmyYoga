from django.shortcuts import render, HttpResponseRedirect
from .forms import CompleteForm
from Database.models import PersonalInformation
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_index,url_login


def customerCompleteInformation(request):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():  # 如果是管理员登陆
        Authority = 'Admin'
    else:  # 如果是客户登陆
        Authority = 'Customer'
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if request.method == 'POST':
        completeForm = CompleteForm(request.POST)
        if completeForm.is_valid():
            name = completeForm.cleaned_data.get('name')
            age = completeForm.cleaned_data.get('age')
            profession = completeForm.cleaned_data.get('profession')
            phoneNumber = completeForm.cleaned_data.get('phoneNumber')
            sex = completeForm.cleaned_data.get('sex')
            birthday = completeForm.cleaned_data.get('birthday')
            height = completeForm.cleaned_data.get('height')
            weight = completeForm.cleaned_data.get('weight')
            bust = completeForm.cleaned_data.get('bust')
            waistline = completeForm.cleaned_data.get('waistline')
            hipline = completeForm.cleaned_data.get('hipline')
            shoulderwidth = completeForm.cleaned_data.get('shoulderwidth')

            username = sessionManager.getUsername()
            personalInformation = PersonalInformation.objects.get(username=username)

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

            return HttpResponseRedirect(url_index)
    else:
        username = sessionManager.getUsername()
        user = PersonalInformation.objects.get(username=username)
        completeForm = CompleteForm(instance=user)
    return render(request, 'personalinformation.html', {'completeForm': completeForm,'Authority': Authority})  # 渲染页面


def viewMemeberList(request):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():  # 如果是管理员登陆
        Authority = 'Admin'
    else:  # 如果是客户登陆
        Authority = 'Customer'
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    userList = PersonalInformation.objects.all()
    detailflag = 'false'
    return render(request, 'personalinformation.html', {'user_list': userList, 'Authority': Authority,
                                                        'detailflag': detailflag })


def viewDetails(request, username):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():  # 如果是管理员登陆
        Authority = 'Admin'
    else:  # 如果是客户登陆
        Authority = 'Customer'
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    userList = PersonalInformation.objects.filter(username=username)
    detailflag = 'true'
    return render(request, 'personalinformation.html', {"user_list": userList,'Authority': Authority, 'detailflag': detailflag})
