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
    if request.method == 'POST':
        temp = CourseForm(request.POST)  # 获取表单内容
        if temp.is_valid():  # 解析表单
            user_name = temp.cleaned_data.get('username')
            course_name= temp.cleaned_data.get('coursename')
            temp=str(user_name)+"/"+str(course_name)
            return HttpResponseRedirect(temp)
    else:
        temp = CourseForm()
    return render(request, 'buycourserightnow.html', locals())

def makebuycourse(request, user_name, course_name):
    course = models.Course.objects.get(coursename=course_name)
    p = models.BuyRecord()
    p.username = user_name
    p.coursename = course.getCourseName()
    p.amount = course.getCoursePrice()
    p.setPayFlag(True)
    p.save()
    return render(request,'mkscourse.html', locals())
