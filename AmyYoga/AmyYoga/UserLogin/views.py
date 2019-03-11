from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from .models import Customer as UserDB


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserDB.objects.get(username=username)
            except(ObjectDoesNotExist):
                return HttpResponse("ObjectDoesNotExist")
            # else:

    else:
        if request.session.get('loginStatus', default=None) is not None:
            return HttpResponsePermanentRedirect('/')
        else:
            form = LoginForm()
            return render(request, 'loginUI.html', {'loginForm': form})
