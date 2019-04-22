from django.shortcuts import render


def teacherteam(request):  # 师资团队页面
    return render(request, 'teacherteam.html')


def yoga(request):  # 瑜伽科普
    return render(request, 'yogamessage.html')


def location(request):  # 场地相关
    return render(request, 'location.html')


def course(request):  # 课程相关
    return render(request, 'course.html')
