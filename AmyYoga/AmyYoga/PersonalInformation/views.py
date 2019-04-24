from django.shortcuts import render, HttpResponseRedirect
from .forms import CompleteForm
from Database.models import PersonalInformation
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_index, url_index_admin, url_index_customer, url_login


def customerCompleteInformation(request):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():  # 如果是管理员登陆
        people = 'guanliyuan'
    else:  # 如果是客户登陆
        people = 'kehu'

    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_admin)
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

            return HttpResponseRedirect(url_index_customer)
    else:
        username = sessionManager.getUsername()
        user = PersonalInformation.objects.get(username=username)
        completeForm = CompleteForm(instance=user)
    return render(request, 'CompleteInfo.html', {'completeForm': completeForm,"people":people})  # 渲染页面


def viewMemeberList(request):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():  # 如果是管理员登陆
        people = 'guanliyuan'
    else:  # 如果是客户登陆
        people = 'kehu'
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    userList = PersonalInformation.objects.all()
    return render(request, 'MemberList.html', {'user_list': userList,"people":people})


def viewDetails(request, username):
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator():  # 如果是管理员登陆
        people = 'guanliyuan'
    else:  # 如果是客户登陆
        people = 'kehu'
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    userList = PersonalInformation.objects.filter(username=username)
    return render(request, 'DetailedInfo.html', {"user_list": userList,"people":people})
