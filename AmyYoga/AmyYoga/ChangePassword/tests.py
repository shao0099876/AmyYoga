from django.test import TestCase
from Database.models import *


# Create your tests here.
class ChangePasswordTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin", authoritySignal=True, password="test_admin_password")
        Customer.objects.create(username="test_customer", password="test_customer_password")

    def test_user_logout_visit(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Offline'
        session.save()
        response = c.get("/changepassword/", follow=True)
        self.assertRedirects(response, "/forgetpasswordlogin/")

    def test_customer_logined_visit(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.get('/changepassword/')
        self.assertTemplateUsed(response, "ChangePasswordUI.html")
    def test_admin_logined_visit(self):
        c=self.client
        session=self.client.session
        session['LoginStatus']='Online'
        session['Authority']='Administrator'
        session['Username']='test_admin'
        session.save()
        response=c.get('/changepassword/')
        print(response.context)
        self.assertHTMLEqual(response.context,'<html><head></head><body>管理员禁止使用修改密码功能</body></html>')
        #self.assertContains(response,"管理员禁止使用修改密码功能")