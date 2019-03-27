from django.shortcuts import render

# Create your views here.
def index(request):#首页页面
    return render(request, 'indexUI.html', locals())  # 渲染页面

def teacherteam(request):#师资团队页面
    return render(request, 'teacherteamUI.html', locals())  # 渲染页面

def yogamessage(request):#瑜伽科普
    return render(request, 'yogamessageUI.html', locals())  # 渲染页面

def aboutlocation(request):#场地相关
    return render(request, 'aboutlocationUI.html', locals())  # 渲染页面

def aboutclass(request):#课程相关
    return render(request, 'aboutclassUI.html', locals())  # 渲染页面

def customerloginedindex(request):#客户登陆过后显示的首界面
    return render(request, 'CustomerLoginedIndexUI.html', locals())  # 渲染页面

def administratorloginedindex(request):#管理员登陆过后的首界面
    return render(request, 'AdministratorLoginedIndexUI.html', locals())  # 渲染页面

