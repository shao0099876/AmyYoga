from django.shortcuts import render
from Database.models import BuyRecord #用户购买课程的记录
from Tools import SessionManager

# Create your views here.

def customercourse(request):  # 向页面输出当前用户已支付的订单信息
    username = SessionManager.getUsername(request) #获取当前登录的用户名字
    user=BuyRecord.objects.filter(username=username,pay_flag=True,valid=True)#获取当前用户已经支付的课程信息
    return render(request, 'customercourseUI.html', {'order':user})  # 渲染页面 按照课程名排序

def uncustomercourse(request): #向页面输出当前用户未支付的订单信息
    username = SessionManager.getUsername(request)  # 获取当前登录的用户名字
    user = BuyRecord.objects.filter(username=username, pay_flag=False,valid=True)  # 获取当前用户未支付的课程信息
    return render(request, 'uncustomercourseUI.html', {'order':user})  # 渲染页面 按照课程名排序

def cancelorder(request,number):#取消订单
    username = SessionManager.getUsername(request)  # 获取当前登录的用户名字
    Q=BuyRecord.objects.get(username=username,number=number) #获取当前用户点击的订单对象
    Q.setValid(False) #将找到的对象相应的位置为false，表明当前订单为取消状态
    return render(request, 'successUI.html',locals())  # 返回修改成功信息