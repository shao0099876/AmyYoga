from django.shortcuts import render
from Database import models
from django.http import HttpResponseRedirect
# Create your views here.
def CourseUsed (request):
    if request.method == 'POST':
        username = request.POST.get('vipname')
        course_name = request.POST.get('coursename')

        if course_name=='all':
            if username=='all':
                user_list = models.user_course_used.objects.all()
            else:
                user_list = models.user_course_used.objects.filter(username=username)
        else:
            if username=='all':
                user_list = models.user_course_used.objects.filter(coursename=course_name)
            else:
                user_list = models.user_course_used.objects.filter(username=username,coursename=course_name)
    return render(request, 'CourseUsed.html', locals())

def moremessage(request, record_id):
    user_list = models.user_course_used.objects.filter(record_id=record_id)
    return render(request, 'CourseOpt.html',locals() )

def newrecord(request,record_id):
    return render(request,'CourseOpt.html',locals())