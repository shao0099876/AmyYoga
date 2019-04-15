from django.shortcuts import render

# Create your views here.
def CourseUsed (request):
    return render(request, 'CourseUsed.html', locals())
#输入筛选条件 会员名 课程名
#显示出一条记录
#此条记录可编辑以上次数