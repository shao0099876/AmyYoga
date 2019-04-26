from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_login,url_index_logined
from Database.models import Course,BuyRecord
from .forms import CourseForm

def purchaseCourse(request):
    '''可以删除这段，将对应功能放在Course的view中，判断用户身份，会员则渲染出购买按钮，导向下面的purchase视图函数'''
    sessionManager=SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_login)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_admin)
    course_list = Course.objects.filter(course_flag=True)
    return render(request, 'coursemessageUI.html', locals())


def purchase(request, course):
    '''修正为提交表单到此处，去除url传递过来的参数，使用表单数据，表单包含coursename，username，amount
    数据表的amount字段项应当保存为订单中购买课的数量，显示总额时应当实时查询数据库实时计算'''
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