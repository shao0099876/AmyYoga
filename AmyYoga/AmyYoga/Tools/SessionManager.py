from .Const import *


def setUsername(request, username):
    request.session['Username'] = username


def setAuthority(request, authority):
    request.session['Authority'] = authority


def setLoginStatus(request, loginStatus):
    request.session['LoginStatus'] = loginStatus


def setLogin(request, username, authoritysign):
    if authoritysign:
        authority = AUTHORITY_ADMINISTRATOR
    else:
        authority = AUTHORITY_CUSTOMER
    setUsername(request, username)
    setAuthority(request, authority)
    setLoginStatus(request, SESSION_LOGINSTATUS_ONLINE)


def isLogined(request):
    if request.session.get('LoginStatus', default=SESSION_LOGINSTATUS_OFFLINE) == SESSION_LOGINSTATUS_ONLINE:
        return True
    else:
        return False


def setLogout(request):
    request.session['LoginStatus'] = SESSION_LOGINSTATUS_OFFLINE
    del request.session['Username']
    del request.session['Authority']


def isLogouted(request):
    if request.session.get('LoginStatus', default=SESSION_LOGINSTATUS_OFFLINE) == SESSION_LOGINSTATUS_OFFLINE:
        return True
    else:
        return False


def isAdministrator(request):
    if request.session.get('Authority', default=AUTHORITY_CUSTOMER) == AUTHORITY_ADMINISTRATOR:
        return True
    else:
        return False


def getUsername(request):
    return request.session.get('Username', default=None)
