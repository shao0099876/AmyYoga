from django.shortcuts import render
from Tools.SessionManager import SessionManager

def teacherteam(request):  # 师资团队页面
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():#如果是登陆状态，那么对应页面就应该显示登出
        status = 'LOGIN'
    else: #如果是未登录状态，那么对应页面就应该显示登陆或者注册
        status = 'LOGOUT'
    return render(request, 'teacherteam.html', {"status": status})


def yoga(request):  # 瑜伽科普
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():#如果是登陆状态，那么对应页面就应该显示登出
        status = 'LOGIN'
    else: #如果是未登录状态，那么对应页面就应该显示登陆或者注册
        status = 'LOGOUT'
    return render(request, 'yoga.html', {"status": status})


def location(request):  # 场地相关
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():  # 如果是登陆状态，那么对应页面就应该显示登出
        status = 'LOGIN'
    else:  # 如果是未登录状态，那么对应页面就应该显示登陆或者注册
        status = 'LOGOUT'
    return render(request, 'location.html', {"status": status})


def course(request):  # 课程相关
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():  # 如果是登陆状态，那么对应页面就应该显示登出
        status = 'LOGIN'
    else:  # 如果是未登录状态，那么对应页面就应该显示登陆或者注册
        status = 'LOGOUT'
    return render(request, 'course.html', {"status": status})
