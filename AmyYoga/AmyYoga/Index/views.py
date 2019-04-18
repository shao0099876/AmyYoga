from django.shortcuts import render


# Create your views here.
def index(request):  # 首页页面
    return render(request, 'indexUI.html', locals())  # 渲染页面


def customerloginedindex(request):  # 客户登陆过后显示的首界面
    return render(request, 'CustomerLoginedIndexUI.html', locals())  # 渲染页面


def administratorloginedindex(request):  # 管理员登陆过后的首界面
    return render(request, 'AdministratorLoginedIndexUI.html', locals())  # 渲染页面
