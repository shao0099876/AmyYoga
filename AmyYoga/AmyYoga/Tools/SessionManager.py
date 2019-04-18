from Database.models import *
SESSION_LOGINSTATUS_ONLINE = 'Online'
SESSION_LOGINSTATUS_OFFLINE = 'Offline'
class SessionManager:
    session = None

    def __init__(self, request=None):
        if request is not None:
            self.session = request.session

    def setUsername(self, username):
        self.session['Username'] = username
        self.session.save()

    def setLoginStatus(self, loginStatus):
        self.session['LoginStatus'] = loginStatus
        self.session.save()

    def setLogin(self, username):
        user=Customer.objects.get(username=username)
        self.setUsername(username)
        self.setLoginStatus(SESSION_LOGINSTATUS_ONLINE)

    def isLogined(self):
        if self.session.get('LoginStatus', default=SESSION_LOGINSTATUS_OFFLINE) == SESSION_LOGINSTATUS_ONLINE:
            return True
        else:
            return False

    def setLogout(self):
        self.setLoginStatus(SESSION_LOGINSTATUS_OFFLINE)
        del self.session['Username']

    def isLogouted(self):
        if self.session.get('LoginStatus', default=SESSION_LOGINSTATUS_OFFLINE) == SESSION_LOGINSTATUS_OFFLINE:
            return True
        else:
            return False

    def isAdministrator(self):
        username=self.session.get("Username",default=None)
        if username is not None:
            user=Customer.objects.get(username=username)
            return user.isAdministrator()
        return False

    def getUsername(self):
        return self.session.get('Username', default=None)
