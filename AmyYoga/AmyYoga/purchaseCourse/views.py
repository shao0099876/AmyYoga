from django.shortcuts import render
from Database import models
from Tools.SessionManager import SessionManager
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def purchaseCourse(request):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    course_list = models.Course.objects.filter(course_flag=True)
    return render(request, 'purchaseCourse.html', locals())

def purchase(request, course):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    if request.method == 'GET':
        username_now=SessionManager.getUsername(request)
        course_temp = models.Course.objects.get(coursename=course)
        p = models.BuyRecord()
        p.username = username_now
        p.coursename = course_temp.getCourseName()
        p.amount = course_temp.getCoursePrice()
        p.save()
        return HttpResponse("添加成功")

