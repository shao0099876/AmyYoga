from django.test import TestCase
from Database.models import Customer
from Tools.SessionManager import SessionManager
from Tools.URLPath import url_login, url_logout, url_index, url_index_admin, url_index_customer


# Create your tests here.
class UserLoginTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin", authoritySignal=True, password="test_admin_password")
        Customer.objects.create(username="test_customer", password="test_customer_password")

    def test_user_unlogined_visit(self):
        c = self.client
        response = c.get(url_login)
        self.assertTemplateUsed(response, 'loginUI.html')
        self.assertEqual(response.status_code, 200)

    def test_info_lost_username(self):
        c = self.client
        response = c.post(url_login, {'username': '', 'password': 'test'})
        self.assertFormError(response, "loginForm", "username", "This field is required.")

    def test_info_lost_password(self):
        c = self.client
        response = c.post(url_login, {'username': 'test_admin', 'password': ''})
        self.assertFormError(response, "loginForm", "password", "This field is required.")

    def test_user_logined_visit(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin("test_admin")
        response = c.get(url_login, follow=True)
        self.assertRedirects(response, url_index)

    def test_login_wrongusername(self):
        c = self.client
        response = c.post(url_login, {'username': 'test', 'password': 'test'})
        self.assertFormError(response, "loginForm", None, "用户名不存在")

    def test_login_wrongpassword(self):
        c = self.client
        response = c.post(url_login, {'username': 'test_admin', 'password': 'test'})
        self.assertFormError(response, "loginForm", None, "密码错误")

    def test_admin_login_successfully(self):
        c = self.client
        response = c.post(url_login, {'username': 'test_admin', 'password': 'test_admin_password'})
        self.assertRedirects(response, url_index_admin)
        session = self.client.session
        self.assertEqual("test_admin", session.get("Username"))
        self.assertEqual("Online", session.get("LoginStatus"))

    def test_customer_login_successfully(self):
        c = self.client
        response = c.post(url_login, {'username': 'test_customer', 'password': 'test_customer_password'})
        self.assertRedirects(response, url_index_customer)
        session = self.client.session
        self.assertEqual("test_customer", session.get("Username"))
        self.assertEqual("Online", session.get("LoginStatus"))

    def test_admin_logout(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_admin')
        response = c.get(url_logout, follow=True)
        self.assertRedirects(response, url_index)
        session = self.client.session
        self.assertEqual('Offline', session.get("LoginStatus"))

    def test_customer_logout(self):
        c = self.client
        sessionManager = SessionManager()
        sessionManager.session = self.client.session
        sessionManager.setLogin('test_customer')
        response = c.get(url_logout, follow=True)
        self.assertRedirects(response, url_index)
        session = self.client.session
        self.assertEqual('Offline', session.get("LoginStatus"))
