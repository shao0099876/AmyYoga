import random

from UserLogin.models import SecurityQA as SecurityQADB

from Tools import SessionManager,Const


def getRandomSecurityQuesiton(request):
    username=SessionManager.getUsername(request)
    securityQA=SecurityQADB.objects.get(username=username)
    num=random.randint(1,3)
    return securityQA.getSecurityQuestion(num)