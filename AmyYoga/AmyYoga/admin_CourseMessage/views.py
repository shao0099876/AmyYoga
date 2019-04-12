from django.shortcuts import render, HttpResponseRedirect
from .forms import AddCourseForm
from .forms import ModCourseForm
from Tools import SessionManager,FormsManager
from Database.models import Course #课程信息数据库
from Database.models import BuyRecord#课程购买信息

# Create your views here.

def admin_coursemessage(request):#管理员查看课程信息
    courses=Course.objects.filter(course_flag=True) #查询在使用的课程信息
    return render(request, 'coursemessageUI.html',{'order':courses})

def Coursename(request,coursename):#显示课程的详细信息
    detailcourse=BuyRecord.objects.filter(coursename=coursename,valid=True)#查询这个课程的所有订单，包括付钱和没付钱的
    return render(request, 'detailmessageUI.html', {'order1':detailcourse})

def addcourse(request):#管理员增加课程信息
    if request.method == 'POST':  # 如果请求为表单提交
        addcourseForm = AddCourseForm(request.POST)  # 获取表单内容
        if addcourseForm.is_valid():  # 解析表单
            coursename=FormsManager.getData(addcourseForm,'coursename')
            courseintroduction=FormsManager.getData(addcourseForm,'courseintroduction')
            courseprice=FormsManager.getData(addcourseForm,'courseprice')

            #判断数据是否合法

            #数据合法之后写入数据库
            course=Course()#创建新的课程，在写入数据信息
            course.setCourseName(coursename)
            course.setCourseIntroduction(courseintroduction)
            course.setCoursePrice(courseprice)
            course.setCourseFlag(True) #新添加的课程，默认为可以使用
            return HttpResponseRedirect("/admin_coursemessage/")  # 写成功之后，跳转到查看课程
    else:
        addcourseForm = AddCourseForm()  # 创建表单
        return render(request, 'addcourseUI.html', locals())

def modifycourse(request):#管理员修改课程信息
    coursec = Course.objects.filter(course_flag=True)  # 查询在使用的课程信息
    return render(request, 'modifycourseUI.html', {'order6':coursec})

def ModCourse(request,coursename):#实际修改课程信息界面
    if request.method == 'POST':  # 如果请求为表单提交
        modcourseForm = ModCourseForm(request.POST)  # 获取表单内容
        if modcourseForm.is_valid():  # 解析表单
            courseintroduction=FormsManager.getData(modcourseForm,'courseintroduction')
            courseprice=FormsManager.getData(modcourseForm,'courseprice')

            #判断数据的正确性
            #写数据库
            R = Course.objects.get(coursename=coursename)  # 查询当前修改信息的课程对象
            R.setCourseIntroduction(courseintroduction)
            R.setCoursePrice(courseprice)
            return HttpResponseRedirect("/admin_coursemessage/")  # 写成功之后，跳转到查看课程
    else:
        r=Course.objects.get(coursename=coursename) #查询当前课程的信息
        modcourseForm = ModCourseForm(instance=r)  # 创建表单
        return render(request, 'modcourseUI.html', locals())

def deletecourse(request):#管理员下架课程
    course = Course.objects.filter(course_flag=True)  # 查询在使用的课程信息
    return render(request, 'deletecourseUI.html', {'order4':course})

def DelCourse(request,coursename):#实际执行下架操作
    P=Course.objects.get(coursename=coursename) #先获取当前课程信息
    P.setCourseFlag(False) #下架课程
    return render(request, 'successfulUI.html', locals())

def readdcourse(request):#管理员重新上架课程信息
    coursee=Course.objects.filter(course_flag=False) #获取已经下架的课程信息
    return render(request, 'readdcourseUI.html', {'order5':coursee})

def reAddCourse(request,coursename):#实际执行重新上架操作
    P = Course.objects.get(coursename=coursename)  # 先获取当前课程信息
    P.setCourseFlag(True)  # 重新上架课程
    return render(request, 'successfulUI.html', locals())