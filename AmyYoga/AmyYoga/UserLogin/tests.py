from django.core.exceptions import ValidationError
from django.test import TestCase,Client
from Database.models import Customer
from UserLogin.forms import LoginForm
from Tools.Const import *
# Create your tests here.
class UserLoginTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin",authoritySignal=True,password="test_admin_password")
        Customer.objects.create(username="test_customer",password="test_customer_password")
    def test_user_unlogined_visit(self):
        c=Client()
        session=c.session
        session['LoginStatus']=SESSION_LOGINSTATUS_OFFLINE
        response=c.get('/login/')
        self.assertEqual(response.status_code, 200)
    def test_info_lost_username(self):
        c=Client()
        response=c.post('/login/',{'username':'','password':'test'})
        self.assertFormError(response,"loginForm","username","This field is required.")
    def test_info_lost_password(self):
        c=Client()
        response=c.post('/login/',{'username':'test_admin','password':''})
        self.assertFormError(response,"loginForm","password","This field is required.")
    def test_user_logined_visit(self):
        c=Client(follow=True)
        c.session['LoginStatus']=SESSION_LOGINSTATUS_ONLINE
        response=c.get("/login/")
        self.assertRedirects(response,"/",)