from django.http import HttpResponseRedirect
from django.shortcuts import render
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_index, url_index_customer, url_index_admin


# Create your views here.
def index(request):  # 首页页面
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():#如果是登陆状态，那么对应页面就应该显示登出
        status = 'LOGOUT'
    else: #如果是未登录状态，那么对应页面就应该显示登陆或者注册
        status = 'LOGIN'
    return render(request, 'Index.html',{"status": status})  # 渲染页面


def customerIndex(request):  # 客户登陆过后显示的首界面
    sessionManager = SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_index)
    if sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_admin)
    people = 'kehu'
    return render(request, 'CustomerIndex.html', {"people": people})  # 渲染页面，传递参数


def adminIndex(request):  # 管理员登陆过后的首界面
    sessionManager = SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_index)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    people = 'guanliyuan'
    return render(request, 'AdminIndex.html', {"people": people})  # 渲染页面，传递参数
