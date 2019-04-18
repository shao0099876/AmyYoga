from django.shortcuts import render


# Create your views here.
def teacherteam(request):  # 师资团队页面
    return render(request, 'teacherteamUI.html', locals())  # 渲染页面


def yogamessage(request):  # 瑜伽科普
    return render(request, 'yogamessageUI.html', locals())  # 渲染页面


def location(request):  # 场地相关
    return render(request, 'aboutlocationUI.html', locals())  # 渲染页面


def course(request):  # 课程相关
    return render(request, 'aboutclassUI.html', locals())  # 渲染页面