from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_login,url_index_admin,url_index_customer
from Database.models import Course,BuyRecord
from .forms import CourseForm

def purchaseCourse(request):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_admin)
    course_list = Course.objects.filter(course_flag=True)
    return render(request, 'purchaseCourse.html', locals())


def purchase(request, course):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_admin)
    if request.method == 'GET':
        username_now=sessionManager.getUsername()
        course_temp = Course.objects.get(coursename=course)
        p = BuyRecord()
        p.username = username_now
        p.coursename = course_temp.getCourseName()
        p.amount = course_temp.getCoursePrice()
        p.save()
        return HttpResponse("添加成功")


def buycourse(request):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    temp = CourseForm()
    return render(request, 'buycourserightnow.html', locals())


def makebuycourse(request):
    if request.method == 'POST':
        temp = CourseForm(request.POST)  # 获取表单内容
        if temp.is_valid():  # 解析表单
            username = temp.cleaned_data.get('username')
            coursename = temp.cleaned_data.get('coursename')
            course = Course.objects.get(coursename=coursename)
            p = BuyRecord()
            p.username = username
            p.coursename = course.getCourseName()
            p.amount = course.getCoursePrice()
            p.setPayFlag(True)
            p.save()
            return render(request, 'mkscourse.html', locals())
    else:
        temp = CourseForm()
    return render(request, 'buycourserightnow.html', locals())


def showtherecord(request):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    record_list = BuyRecord.objects.filter(valid=True)
    return render(request, 'showrecord.html', locals())


def detailrecord(request, recordid):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    item = BuyRecord.objects.get(number=recordid)
    return render(request, 'therecord.html', locals())


def makerecord(request, cord):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    item = BuyRecord.objects.get(number=cord)
    item.setPayFlag(True)
    return render(request, 'therecord.html', locals())


def canclerecord(request, discord):
    sessionManager = SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    item = BuyRecord.objects.get(number=discord)
    item.setValid(False)
    return render(request, 'therecord.html', locals())
