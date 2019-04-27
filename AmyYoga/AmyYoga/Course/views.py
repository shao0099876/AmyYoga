from django.http import HttpResponseRedirect
from django.shortcuts import render
from Database.models import BuyRecord, Course  # 用户购买课程的记录
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_index, url_course_view_course
from .forms import AddCourseForm, ModCourseForm


def viewCourse(request):  # 管理员查看课程信息
    '''这个功能换成通用的，管理员访问在模板生成时多加个修改的按钮'''
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator(): #如果是管理员登陆
        courses = Course.objects.all()  # 查询全部课程信息
        Authority = 'Admin'

    else: #如果是客户登陆
        courses = Course.objects.filter(course_flag=True)  # 查询在使用的课程信息
        Authority = 'Customer'

    return render(request, 'coursemessageUI.html', {'order': courses, 'Authority': Authority})


def viewCourseDetails(request, coursename):  # 显示课程的详细信息
    '''修改此处功能，换成显示课程的课程名，简介等信息'''
    sessionManager = SessionManager(request)
    if sessionManager.isAdministrator(): #如果是管理员登陆
        courses = Course.objects.get(coursename=coursename)  # 查询当前课程信息,为了后面显示详细信息
        detailcourse = BuyRecord.objects.filter(coursename=coursename)  # 查询这个课程的所有订单（包括付钱和没付钱的）
        Authority = 'Admin'

    else: #如果是客户登陆
        username = sessionManager.getUsername()  # 获取当前登录的用户名字
        courses = Course.objects.get(coursename=coursename)  # 查询当前课程信息,为了后面显示详细信息
        detailcourse = BuyRecord.objects.filter(username=username,coursename=coursename)  # 查询这个用户关于这门课的订单状态（付钱和没付钱的）
        Authority = 'Customer'
    return render(request, 'detailmessageUI.html', {'Authority': Authority, 'courses':courses,'order1': detailcourse})


def addCourse(request):  # 管理员增加课程信息
    sessionManager = SessionManager(request)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    if request.method == 'POST':
        addcourseForm = AddCourseForm(request.POST)
        if addcourseForm.is_valid():
            coursename = addcourseForm.cleaned_data.get('coursename')
            courseintroduction = addcourseForm.cleaned_data.get('courseintroduction')
            courseprice = addcourseForm.cleaned_data.get('courseprice')
            course = Course()
            course.create(coursename,courseintroduction,courseprice)
            return HttpResponseRedirect(url_course_view_course)
    else:
        addcourseForm = AddCourseForm()
        return render(request, 'addcourseUI.html', locals())


def ModCourse(request, coursename):  # 实际修改课程信息界面
    '''等待转换为主修改视图函数'''
    sessionManager = SessionManager(request)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    if request.method == 'POST':  # 如果请求为表单提交
        modcourseForm = ModCourseForm(request.POST)  # 获取表单内容
        if modcourseForm.is_valid():  # 解析表单
            courseintroduction = modcourseForm.cleaned_data['courseintroduction']
            courseprice = modcourseForm.cleaned_data['courseprice']
            R = Course.objects.get(coursename=coursename)  # 查询当前修改信息的课程对象
            R.setCourseIntroduction(courseintroduction)
            R.setCoursePrice(courseprice)
            return HttpResponseRedirect(url_course_view_course)  # 写成功之后，跳转到查看课程
    else:
        r = Course.objects.get(coursename=coursename)  # 查询当前课程的信息
        modcourseForm = ModCourseForm(instance=r)  # 创建表单
        return render(request, 'modcourseUI.html', locals())


def DelCourse(request, coursename):  # 实际执行下架操作
    '''等待转换为主视图函数'''
    sessionManager = SessionManager(request)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    P = Course.objects.get(coursename=coursename)  # 先获取当前课程信息
    P.setCourseFlag(False)  # 下架课程
    return render(request, 'successfulUI.html', locals())


def reAddCourse(request, coursename):  # 实际执行重新上架操作
    '''等待转换为主视图函数'''
    sessionManager = SessionManager(request)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index)
    P = Course.objects.get(coursename=coursename)  # 先获取当前课程信息
    P.setCourseFlag(True)  # 重新上架课程
    return render(request, 'successfulUI.html', locals())

