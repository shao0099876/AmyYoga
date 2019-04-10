from django.shortcuts import render
from Database.models import Course #课程信息数据库
from Database.models import BuyRecord#课程购买信息

# Create your views here.

def admin_coursemessage(request):#管理员查看课程信息
    courses=Course.objects.all()#查询课程
    return render(request, 'coursemessageUI.html',{'order':courses})

def Coursename(request,coursename):#显示课程的详细信息
    detailcourse=BuyRecord.objects.filter(coursename=coursename,valid=True)#查询这个课程的所有订单，包括付钱和没付钱的
    return render(request, 'detailmessageUI.html', {'order1':detailcourse})

def addcourse(request):#管理员增加课程信息
    return render(request, 'addcourseUI.html', locals())

def modifycourse(request):#管理员修改课程信息
    return render(request, 'modifycourseUI.html', locals())

def deletecourse(request):#管理员下架课程
    return render(request, 'deletecourseUI.html', locals())

def readdcourse(request):#管理员重新上架课程信息
    return render(request, 'readdcourseUI.html', locals())
