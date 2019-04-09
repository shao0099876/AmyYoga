from django.shortcuts import render
from Database.models import BuyCourse as buyCourseDB #已支付课程记录，需要修改
from Database.models import BuyedCourse as buyedCourseDB #未支付课程记录，需要修改
from Tools import SessionManager,FormsManager

# Create your views here.

def customercourse(request):  # 向页面输出当前用户已支付的订单信息
    username = SessionManager.getUsername(request) #获取当前登录的用户名字
    user=buyCourseDB.objects.filter(username=username)



    return render(request, 'customercourseUI.html', locals())  # 渲染页面 按照课程名排序


def uncustomercourse(request): #向页面输出当前用户未支付的订单信息
    username = SessionManager.getUsername(request)  # 获取当前登录的用户名字

    return render(request, 'uncustomercourseUI.html', locals())  # 渲染页面 按照课程名排序