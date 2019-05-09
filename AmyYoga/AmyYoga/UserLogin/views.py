from django.shortcuts import render, HttpResponseRedirect
from Tools.SessionManager import SessionManager
from .forms import LoginForm
from Database.models import Customer
from Tools.URLPath import url_index_logined,url_index


# Create your views here.
def login(request):
    sessionManager = SessionManager(request)
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')
            user = Customer.objects.get(username=username)
            sessionManager.setLogin(username)
            return HttpResponseRedirect(url_index_logined)
    else:
        if sessionManager.isLogined():
            return HttpResponseRedirect(url_index)
        else:
            loginForm = LoginForm()
    return render(request, 'loginUI.html', {'loginForm': loginForm})


def logout(request):
    sessionManager = SessionManager(request)
    if sessionManager.isLogined():
        sessionManager.setLogout()
    return HttpResponseRedirect(url_index)

