from django.shortcuts import render
from Database import models
import datetime
from Tools.SessionManager import SessionManager
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
# Create your views here.
def CourseUsed (request):
    username_app=models.Course.objects.all()
    Authority = 'Admin'
    if request.method == 'POST':
        if request.POST.get('Submit'):#如果是Submit传来的请求
            username = request.POST.get('vipname')
            course_name = request.POST.get('coursename')
            if course_name=='all':
                if username=='all':
                    user_list = models.CourseUsedRecord.objects.all()
                    used_times = 0
                else:
                    user_list = models.CourseUsedRecord.objects.filter(username=username)
                    used_times = 0
            else:
                if username=='all':
                    user_list = models.CourseUsedRecord.objects.filter(coursename=course_name)
                    used_times = 0
                else:
                    user_list = models.CourseUsedRecord.objects.filter(username=username,coursename=course_name)
                    used_times= models.CourseUsedRecord.objects.filter(username=username,coursename=course_name).count()
        else:
            if request.POST.get('newlyRecord'):#如果是newlyRecord传来的请求
                username = request.POST.get('vipname')
                course_name = request.POST.get('coursename')
                flags=models.Customer.objects.filter(username=username).exists()
                if username==''or username=='all' or course_name=='' or course_name=='all'or flags==False:#用户名为空
                    messages.warning(request, "输入错误！")
                    return render(request, 'CourseUsed.html', locals())#跳转
                else:#在username,course_name新建一条数据库记录，自动生成一个id作为主键
                    year=datetime.datetime.now().year
                    month=datetime.datetime.now().month
                    day = datetime.datetime.now().day
                    hour=datetime.datetime.now().hour
                    minute=datetime.datetime.now().minute
                    second=datetime.datetime.now().second
                    microsecond=datetime.datetime.now().microsecond

                    timeid=str(year)+fixformats(month)+fixformats(day)+fixformats(hour)+fixformats(minute)+fixformats(second)+fixformats(microsecond)
                    models.CourseUsedRecord.objects.create(timeid=timeid, username=username, coursename=course_name)
                    return render(request, 'CourseUsed.html', locals())
    return render(request, 'CourseUsed.html', locals())
def moremessage_username(request, username):
    user_list = models.CourseUsedRecord.objects.filter(username=username)
    return render(request, 'CourseOpt.html',locals() )
    #return render(request, 'UserCourseUsedRecord.html', locals())
def moremessage_coursename(request, coursename):
    user_list = models.CourseUsedRecord.objects.filter(coursename=coursename)
    #return render(request, 'CourseOpt.html',locals() )
    return render(request, 'UserCourseUsedRecord.html', locals())
def fixformats(date):
    if date//10==0:
        return '0'+str(date)
    else:
        return str(date)
def UserCourseUsed(request):
    sessionManager = SessionManager(request)
    username = sessionManager.getUsername()
    Authority = 'Customer'
    if request.method == 'POST':
        coursename = request.POST.get('coursename')
        if coursename=='all':
            user_list = models.CourseUsedRecord.objects.filter(username=username)
            used_times = 0
        else:
            user_list = models.CourseUsedRecord.objects.filter(username=username,coursename=coursename)
            used_times= models.CourseUsedRecord.objects.filter(username=username,coursename=coursename).count()
    return render(request, 'UserCourseUsedRecord.html',locals() )