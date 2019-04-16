from django.shortcuts import render
from Database import models
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

def plus(request):

    return render(request,'CourseUsed.html',locals())
#输入筛选条件 会员名 课程名
#显示出一条记录
#此条记录可编辑已上次数