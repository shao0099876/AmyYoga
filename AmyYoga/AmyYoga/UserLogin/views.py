from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    if request.session.get('loginStatus',default=None) is not None:
        return HttpResponsePermanentRedirect('/')
    else:
        #return render('loginUI.html')
        return HttpResponse('render(loginUI.html)')
