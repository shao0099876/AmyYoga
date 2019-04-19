from django.shortcuts import render ,HttpResponseRedirect,HttpResponse
from Tools.SessionManager import SessionManager
from .forms import CourseForm
from Database import models
# Create your views here.
def buycourse(request):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    temp = CourseForm()
    return render(request,'buycourserightnow.html', locals())

def makebuycourse(request):
    sessionManager = SessionManager(request)
    if request.method == 'POST':
        temp = CourseForm(request.POST)  # 获取表单内容
        if temp.is_valid():  # 解析表单
            username = temp.cleaned_data.get('username')
            coursename= temp.cleaned_data.get('coursename')
            course = models.Course.objects.get(coursename=coursename)
            p = models.BuyRecord()
            p.username = username
            p.coursename = course.getCourseName()
            p.amount = course.getCoursePrice()
            p.setPayFlag(True)
            p.save()
            return render(request,'mkscourse.html', locals())
    else:
        temp = CourseForm()
    return render(request,'buycourserightnow.html', locals())
