from django.shortcuts import render
from Database.models import Course, CourseUsedRecord, Customer
import datetime
from Tools.SessionManager import SessionManager
from django.contrib import messages
def CourseUsed(request):
    '''全面更换form'''
    username_app = Course.objects.all()    if request.method == 'POST':
        if request.POST.get('Submit'):  # 如果是Submit传来的请求
            username = request.POST.get('vipname')
            course_name = request.POST.get('coursename')
            if course_name == 'all':
                if username == 'all':
                    user_list = CourseUsedRecord.objects.all()
                    used_times = 0
                else:
                    user_list = CourseUsedRecord.objects.filter(username=username)
                    used_times = 0
            else:
                if username == 'all':
                    user_list = CourseUsedRecord.objects.filter(coursename=course_name)
                    used_times = 0
                else:
                    user_list = CourseUsedRecord.objects.filter(username=username, coursename=course_name)
                    used_times = CourseUsedRecord.objects.filter(username=username, coursename=course_name).count()
        else:
            if request.POST.get('newlyRecord'):  # 如果是newlyRecord传来的请求
                username = request.POST.get('vipname')
                course_name = request.POST.get('coursename')
                '''因为username就是主键，所以修正这个写法为get，默认返回值设置为None，后面判断是不是none即可'''
                flags = Customer.objects.filter(username=username).exists()
                if username == '' or username == 'all' or course_name == '' or course_name == 'all' or flags == False:  # 用户名为空
                    messages.warning(request, "输入错误！")
                    return render(request, 'CourseUsed.html', locals())  # 跳转
                else:  # 在username,course_name新建一条数据库记录，自动生成一个id作为主键
                    '''使用递增数字作为主键，时间作为新字段属性'''
                    new_number = 1
                    CourseUsedRecord.objects.create(number=new_number, username=username, coursename=course_name)
                    return render(request, 'CourseUsed.html', locals())
    return render(request, 'CourseUsed.html', locals())


def moremessage_username(request, username):
    user_list = CourseUsedRecord.objects.filter(username=username)
    return render(request, 'CourseOpt.html', locals())


def moremessage_coursename(request, coursename):
    user_list = CourseUsedRecord.objects.filter(coursename=coursename)
    return render(request, 'UserCourseUsedRecord.html', locals())


def UserCourseUsed(request):
    sessionManager=SessionManager(request)
    username=sessionManager.getUsername()
    if request.method == 'POST':
        coursename = request.POST.get('coursename')
        if coursename == 'all':
            user_list = CourseUsedRecord.objects.filter(username=username)
            used_times = 0
        else:
            user_list = CourseUsedRecord.objects.filter(username=username, coursename=coursename)
            used_times = CourseUsedRecord.objects.filter(username=username, coursename=coursename).count()
    return render(request, 'UserCourseUsedRecord.html', locals())
