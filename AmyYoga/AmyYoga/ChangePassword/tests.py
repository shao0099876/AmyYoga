from django.test import TestCase
from Database.models import Customer
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_change_password,url_forget_password,url_forget_password_login,url_login,url_index_customer

# Create your tests here.
class ChangePasswordTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin", authoritySignal=True, password="test_admin_password")
        Customer.objects.create(username="test_customer", password="test_customer_password")

    def test_ChangePassword_successChange(self):
        c = self.client
        sessionManager=SessionManager()
        sessionManager.session=self.client.session
        sessionManager.setLogin('test_customer')
        response = c.post(url_change_password,
                          {'oldPassword': 'test_customer_password', 'newPassword': 'test123',
                           'confirmPassword': "test123"}, follow=True)
        self.assertRedirects(response, url_login)
        response = c.post('/login/', {'username': 'test_customer', 'password': 'test123'}, follow=True)
        self.assertRedirects(response, url_index_customer)
        session = self.client.session
        self.assertEqual("test_customer", session.get("Username"))
        self.assertEqual("Online", session.get("LoginStatus"))

    def test_ForgetPassword_success(self):
        c = self.client
        sessionManager=SessionManager()
        sessionManager.session=self.client.session
        response=c.post(url_forget_password_login,{'username':'test_customer'})
        self.assertRedirects(response,url_forget_password)
        response = c.post(url_forget_password, {'newPassword': 'abc123', 'confirmPassword': 'abc123'}, follow=True)
        self.assertRedirects(response, url_login)
        response = c.post(url_login, {'username': 'test_customer', 'password': 'abc123'}, follow=True)
        self.assertRedirects(response, url_index_customer)
        session = self.client.session
        self.assertEqual("test_customer", session.get("Username"))
        self.assertEqual("Online", session.get("LoginStatus"))
