from django.shortcuts import render

# Create your views here.
def customerbuycourse(request):
    return render(request, 'customerbuycourseUI.html', locals())  # 渲染页面