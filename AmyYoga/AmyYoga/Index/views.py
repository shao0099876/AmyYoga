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
    return render(request, 'CustomerIndex.html')  # 渲染页面


def adminIndex(request):  # 管理员登陆过后的首界面
    sessionManager = SessionManager(request)
    if sessionManager.isLogouted():
        return HttpResponseRedirect(url_index)
    if not sessionManager.isAdministrator():
        return HttpResponseRedirect(url_index_customer)
    return render(request, 'AdminIndex.html')  # 渲染页面
