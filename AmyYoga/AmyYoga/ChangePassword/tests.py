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
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Administrator'
        session['Username'] = 'test_admin'
        session.save()
        response = c.get('/changepassword/')
        self.assertEqual(response.content.decode(), '管理员禁止使用修改密码功能')

    def test_ChangePassword_lostinfo1(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': '', 'newPassword': 'test123', 'confirmPassword': "test123"})
        self.assertFormError(response, 'changePasswordForm', 'oldPassword', 'This field is required.')

    def test_ChangePassword_lostinfo2(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': 'test_customer_password', 'newPassword': '', 'confirmPassword': "test123"})
        self.assertFormError(response, 'changePasswordForm', 'newPassword', 'This field is required.')

    def test_ChangePassword_lostinfo3(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': 'test_customer_password', 'newPassword': 'test123', 'confirmPassword': ""})
        self.assertFormError(response, 'changePasswordForm', 'confirmPassword', 'This field is required.')

    def test_ChangePassword_wrong_oldPassword(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': 'test_customer_passwor', 'newPassword': 'test123',
                           'confirmPassword': "test123"})
        self.assertFormError(response, 'changePasswordForm', None, '密码不正确')

    def test_ChangePassword_wrongformat1(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': 'test_customer_password', 'newPassword': 'test',
                           'confirmPassword': "test"})
        self.assertFormError(response, 'changePasswordForm', None, '密码格式不正确')

    def test_ChangePassword_wrongformat2(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': 'test_customer_password', 'newPassword': '123',
                           'confirmPassword': "123"})
        self.assertFormError(response, 'changePasswordForm', None, '密码格式不正确')

    def test_ChangePassword_wrong_confirmPassword(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': 'test_customer_password', 'newPassword': 'test123',
                           'confirmPassword': "test23"})
        self.assertFormError(response, 'changePasswordForm', None, '两次密码不一致')

    def test_ChangePassword_successChange(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session['Authority'] = 'Customer'
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/changepassword/',
                          {'oldPassword': 'test_customer_password', 'newPassword': 'test123',
                           'confirmPassword': "test123"}, follow=True)
        self.assertRedirects(response, '/login/')
        response = c.post('/login/', {'username': 'test_customer', 'password': 'test123'}, follow=True)
        self.assertRedirects(response, '/customerloginedindex/')
        session = self.client.session
        self.assertEqual("test_customer", session.get("Username"))
        self.assertEqual("Customer", session.get("Authority"))
        self.assertEqual("Online", session.get("LoginStatus"))

    def test_ForgetPassword_adminLogined(self):
        c = self.client
        response = c.post('/forgetpasswordlogin/', {'username': 'test_admin'})
        self.assertEqual(response.content.decode(), '管理员禁止使用修改密码功能')

    def test_ForgetPassword_customer_login(self):
        c = self.client
        response = c.post('/forgetpasswordlogin/', {'username': 'test_customer'}, follow=True)
        self.assertRedirects(response, '/forgetpassword/')
        session = self.client.session
        self.assertEqual("test_customer", session.get("Username"))

    def test_ForgetPassword_admin_visit_forgetpassword(self):
        c = self.client
        session = self.client.session
        session['Authority'] = 'Administrator'
        session['Username'] = 'test_admin'
        session.save()
        response = c.get('/forgetpassword/')
        self.assertEqual(response.content.decode(), '管理员禁止使用修改密码功能')

    def test_ForgetPassword_admin_visit_forgetpasswordlogin(self):
        c = self.client
        session = self.client.session
        session['Authority'] = 'Administrator'
        session['Username'] = 'test_admin'
        session.save()
        response = c.get('/forgetpasswordlogin/')
        self.assertEqual(response.content.decode(), '管理员禁止使用修改密码功能')

    def test_ForgetPasswordLogin_lostinfo(self):
        c = self.client
        response = c.post('/forgetpasswordlogin/', {'username': ""})
        self.assertFormError(response, 'usernameForm', 'username', 'This field is required.')

    def test_ForgetPassword_lostinfo1(self):
        c = self.client
        session = self.client.session
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/forgetpassword/', {'newPassword': '', 'confirmPassword': ''})
        self.assertFormError(response, 'forgetPasswordForm', 'newPassword', 'This field is required.')

    def test_ForgetPassword_lostinfo2(self):
        c = self.client
        session = self.client.session
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/forgetpassword/', {'newPassword': 'test123', 'confirmPassword': ''})
        self.assertFormError(response, 'forgetPasswordForm', 'confirmPassword', 'This field is required.')

    def test_ForgetPasswordLogin_username_not_exist(self):
        c = self.client
        response = c.post('/forgetpasswordlogin/', {'username': 'test'})
        self.assertFormError(response, 'usernameForm', None, '用户名不存在')

    def test_ForgetPassword_wrong_format(self):
        c = self.client
        session = self.client.session
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/forgetpassword/', {'newPassword': 'test', 'confirmPassword': 'test'})
        self.assertFormError(response, 'forgetPasswordForm', None, '密码格式不正确')
        response = c.post('/forgetpassword/', {'newPassword': '123', 'confirmPassword': '123'})
        self.assertFormError(response, 'forgetPasswordForm', None, '密码格式不正确')

    def test_ForgetPassword_wrong_confirmPassword(self):
        c = self.client
        session = self.client.session
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/forgetpassword/', {'newPassword': 'test123', 'confirmPassword': 'test12'})
        self.assertFormError(response, 'forgetPasswordForm', None, '两次密码不一致')

    def test_ForgetPassword_success(self):
        c = self.client
        session = self.client.session
        session['Username'] = 'test_customer'
        session.save()
        response = c.post('/forgetpassword/', {'newPassword': 'abc123', 'confirmPassword': 'abc123'},follow=True)

        self.assertRedirects(response, '/login/')
        response = c.post('/login/', {'username': 'test_customer', 'password': 'abc123'}, follow=True)
        self.assertRedirects(response, '/customerloginedindex/')
        session = self.client.session
        self.assertEqual("test_customer", session.get("Username"))
        self.assertEqual("Customer", session.get("Authority"))
        self.assertEqual("Online", session.get("LoginStatus"))