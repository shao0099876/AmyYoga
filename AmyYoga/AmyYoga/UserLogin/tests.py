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
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Offline'
        session.save()
        response=c.get("/login/")
        self.assertEqual(response.status_code, 200)
    def test_info_lost_username(self):
        c=self.client
        response=c.post('/login/',{'username':'','password':'test'})
        self.assertFormError(response,"loginForm","username","This field is required.")
    def test_info_lost_password(self):
        c=self.client
        response=c.post('/login/',{'username':'test_admin','password':''})
        self.assertFormError(response,"loginForm","password","This field is required.")
    def test_user_logined_visit(self):
        c=self.client
        session=self.client.session
        session['LoginStatus']='Online'
        session.save()
        response=c.get("/login/",follow=True)
        self.assertRedirects(response,"/")
    def test_login_wrongusername(self):
        c=self.client
        response = c.post('/login/', {'username': 'test', 'password': 'test'})
        self.assertFormError(response, "loginForm", None, "用户名不存在")
    def test_login_wrongpassword(self):
        c=self.client
        response=c.post('/login/',{'username':'test_admin','password':'test'})
        self.assertFormError(response, "loginForm", None, "密码错误")
    def test_admin_login_successfully(self):
        c=self.client
        response=c.post('/login/',{'username':'test_admin','password':'test_admin_password'})
        self.assertRedirects(response,'/administratorloginedindex/')
        session = self.client.session
        self.assertEqual("test_admin",session.get("Username"))
        self.assertEqual("Administrator",session.get("Authority"))
        self.assertEqual("Online",session.get("LoginStatus"))
    def test_customer_login_successfully(self):
        c=self.client
        response=c.post('/login/',{'username':'test_customer','password':'test_customer_password'})
        self.assertRedirects(response,'/customerloginedindex/')
        session = self.client.session
        self.assertEqual("test_customer",session.get("Username"))
        self.assertEqual("Customer",session.get("Authority"))
        self.assertEqual("Online",session.get("LoginStatus"))