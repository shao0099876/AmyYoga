from django.http import HttpResponse
from django.shortcuts import render
from UserLogin import models

def superusermessage(request):
    #if request.method == 'POST':  # 如果请求为表单提交
    #   return HttpResponse("ok")
    user_list = models.PersonalInformation.objects.all()
    return render(request, 'vipmessage.html', locals())

def moremessage(request, user):
    user_list = models.PersonalInformation.objects.filter(username=user)
    #return HttpResponse(user)
    return render(request, 'moremessage.html',locals() )