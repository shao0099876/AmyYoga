from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_login,url_index_logined,url_index
from Database.models import Course,BuyRecord
from .forms import CourseForm,recordForm

def purchaseCourse(request):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_login)
    Authority = 'Customer'
    course_list = Course.objects.filter(course_flag=True)
    return render(request, 'purchaseCourse.html', {"Authority": Authority,'course_list':course_list})


def purchase(request):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    if request.method == 'POST':
        courserecord = recordForm(request.POST)
        if courserecord.is_valid():
            username_now=sessionManager.getUsername()
            course = courserecord.cleaned_data.get('coursename')
            course_temp = Course.objects.get(coursename=course)
            p = BuyRecord()
            p.number=27
            p.username = username_now
            p.coursename = course_temp.getCourseName()
            p.amount = course_temp.getCoursePrice()
            p.save()
            return HttpResponse("添加成功")
        return HttpResponse("添加失败")


def showtherecord(request):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    Authority = 'Admin'         #表示是管理员身份
    localflag = 'True'          #表示是否在主订单节面，作用实现html文件的复用，下同
    iterable = 'True'           #record_list是否可以迭代
    record_list = BuyRecord.objects.filter(valid=True)
    return render(request, 'showrecord.html', {"Authority": Authority,'record_list':record_list,'localflag':localflag,'iterable':iterable})


def detailrecord(request, recordid):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    Authority = 'Admin'
    localflag = 'Flase'
    iterable = 'Flase'
    record_list = BuyRecord.objects.get(number=recordid)
    return render(request, 'showrecord.html',{"Authority": Authority,'item':record_list,"localflag": localflag,'iterable':iterable} )


def makerecord(request, cord):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    item = BuyRecord.objects.get(number=cord)
    item.setPayFlag(True)
    Authority = 'Admin'
    localflag = 'Flase'
    iterable = 'Flase'
    return render(request, 'showrecord.html', {"Authority": Authority,'item':item,'localflag':localflag,'iterable':iterable})


def canclerecord(request, discord):
    sessionManager = SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    item = BuyRecord.objects.get(number=discord)
    item.setValid(False)
    Authority = 'Admin'
    localflag = 'Flase'
    iterable = 'Flase'
    return render(request, 'showrecord.html', {"Authority": Authority,'item':item,'localflag':localflag,'iterable':iterable})



def buycourse(request):
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    temp = CourseForm()
    Authority = 'Admin'
    return render(request, 'buycourserightnow.html', {"Authority": Authority,'temp':temp})


def makebuycourse(request):
    if request.method == 'POST':
        temp=CourseForm(request.POST)
        if temp.is_valid():  # 解析表单
            username = temp.cleaned_data.get('username')
            coursename = temp.cleaned_data.get('coursename')
            course = Course.objects.get(coursename=coursename)
            p = BuyRecord()
            p.username = username
            p.coursename = course.getCourseName()
            p.amount = course.getCoursePrice()
            p.setPayFlag(False)
            Authority = 'Admin'
            localflag = 'Flase'
            iterable = 'False'
            return render(request, 'showrecord.html', {"Authority": Authority,"item":p, ' localflag':localflag,'iterable':iterable})
    else:
        temp = CourseForm()
    return render(request, 'buycourserightnow.html', locals())


def customercourse(request):  # 向页面输出当前用户已支付的订单信息
    sessionManager = SessionManager(request)
    username = sessionManager.getUsername()  # 获取当前登录的用户名字
    user = BuyRecord.objects.filter(username=username, pay_flag=True, valid=True)  # 获取当前用户已经支付的课程信息
    return render(request, 'customercourseUI.html', {'order': user})  # 渲染页面 按照课程名排序


def uncustomercourse(request):  # 向页面输出当前用户未支付的订单信息
    username = SessionManager.getUsername(request)  # 获取当前登录的用户名字
    user = BuyRecord.objects.filter(username=username, pay_flag=False, valid=True)  # 获取当前用户未支付的课程信息
    return render(request, 'uncustomercourseUI.html', {'order': user})  # 渲染页面 按照课程名排序


def cancelorder(request, number):  # 取消订单
    username = SessionManager.getUsername(request)  # 获取当前登录的用户名字
    Q = BuyRecord.objects.get(username=username, number=number)  # 获取当前用户点击的订单对象
    Q.setValid(False)  # 将找到的对象相应的位置为false，表明当前订单为取消状态
    return render(request, 'successUI.html', locals())  # 返回修改成功信息