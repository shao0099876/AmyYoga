from django.shortcuts import render
from Database.models import BuyCourse as buyCourseDB #购买课程记录，需要修改
from Database.models import BuyedCourse as buyedCourseDB #已消费课程记录，需要修改
from Tools import SessionManager,FormsManager

# Create your views here.

def customercourse(request):  # 向页面输出订单
    username = SessionManager.getUsername(request) #获取当前登录的用户名字

    return render(request, 'customercourseUI.html', locals())  # 渲染页面 按照课程名排序
