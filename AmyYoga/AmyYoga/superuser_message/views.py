from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Database import models
from Tools.SessionManager import SessionManager


def superusermessage(request):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    user_list = models.PersonalInformation.objects.all()
    return render(request, 'vipmessage.html', locals())

def moremessage(request, username):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    user_list = models.PersonalInformation.objects.filter(username=username)
    return render(request, 'moremessage.html',locals() )