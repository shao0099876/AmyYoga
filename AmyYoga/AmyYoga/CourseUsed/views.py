from django.shortcuts import render
from Database import models
import datetime
from django.http import HttpResponseRedirect
# Create your views here.
def CourseUsed (request):
    if request.method == 'POST':
        if request.POST.get('Submit'):#如果是Submit传来的请求
            username = request.POST.get('vipname')
            course_name = request.POST.get('coursename')
            if course_name=='all':
                if username=='all':
                    user_list = models.user_course_used.objects.all()
                    used_times = 0
                else:
                    user_list = models.user_course_used.objects.filter(username=username)
                    used_times = 0
            else:
                if username=='all':
                    user_list = models.user_course_used.objects.filter(coursename=course_name)
                    used_times = 0
                else:
                    user_list = models.user_course_used.objects.filter(username=username,coursename=course_name)
                    used_times= models.user_course_used.objects.filter(username=username,coursename=course_name).count()
        else:
            if request.POST.get('newlyRecord'):#如果是newlyRecord传来的请求
                username = request.POST.get('vipname')
                course_name = request.POST.get('coursename')
                if username==''or username=='all' or course_name=='' or course_name=='all':#用户名为空
                    return render(request, 'CourseOpt.html', locals())#跳转
                else:#在username,course_name新建一条数据库记录，自动生成一个id作为主键
                    year=datetime.datetime.now().year
                    month=datetime.datetime.now().month
                    day = datetime.datetime.now().day
                    hour=datetime.datetime.now().hour
                    minute=datetime.datetime.now().minute
                    second=datetime.datetime.now().second
                    time_id=str(year)+fixformats(month)+fixformats(day)+fixformats(hour)+fixformats(minute)+fixformats(second)
                    models.user_course_used.objects.create(record_id=time_id, username=username, coursename=course_name)
                    return render(request, 'CourseUsed.html', locals())

    return render(request, 'CourseUsed.html', locals())

def moremessage_username(request, username):
    user_list = models.user_course_used.objects.filter(username=username)
    return render(request, 'CourseOpt.html',locals() )
def moremessage_coursename(request, coursename):
    user_list = models.user_course_used.objects.filter(coursename=coursename)
    return render(request, 'CourseOpt.html',locals() )

def newrecord(request,record_id):
    return render(request,'CourseOpt.html',locals())

def fixformats(date):
    if date//10==0:
        return '0'+str(date)
    else:
        return str(date)