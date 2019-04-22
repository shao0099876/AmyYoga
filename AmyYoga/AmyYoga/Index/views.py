from django.http import HttpResponseRedirect
from django.shortcuts import render
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_index, url_index_customer, url_index_admin


# Create your views here.
def index(request):  # 首页页面
    return render(request, 'Index.html')  # 渲染页面


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
