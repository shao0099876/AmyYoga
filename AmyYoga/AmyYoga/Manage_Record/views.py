from django.shortcuts import render ,HttpResponseRedirect
from Tools.SessionManager import SessionManager
from Database import models
def showtherecord(request):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    record_list = models.BuyRecord.objects.filter(valid=True)
    return render(request, 'showrecord.html', locals())

def detailrecord(request,recordid):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    item = models.BuyRecord.objects.get(number=recordid)
    return render(request, 'therecord.html', locals())

def makerecord(request,cord):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    item = models.BuyRecord.objects.get(number=cord)
    item.setPayFlag(True)
    return render(request, 'therecord.html', locals())

def canclerecord(request,discord):
    if SessionManager.isLogouted(request):
        return HttpResponseRedirect("/login/")
    if not SessionManager.isAdministrator(request):
        return HttpResponseRedirect("/")
    item = models.BuyRecord.objects.get(number=discord)
    item.setValid(False)
    return render(request, 'therecord.html', locals())