from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Database import models

from Tools import SessionManager


def superusermessage(request):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    user_list = models.PersonalInformation.objects.all()
    return render(request, 'vipmessage.html', locals())

def moremessage(request, user):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    user_list = models.PersonalInformation.objects.filter(username=user)
    #return HttpResponse(user)
    return render(request, 'moremessage.html',locals() )