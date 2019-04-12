from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from Database.models import *


# Create your tests here.
class CustomerRegisterTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin", authoritySignal=True, password="test_admin_password")
        Customer.objects.create(username="test_customer", password="test_customer_password")

    def test_user_logout_visit(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Offline'
        session.save()
        response = c.get('/register/')
        self.assertTemplateUsed(response, 'registerUI.html')

    def test_user_logined_visit(self):
        c = self.client
        session = self.client.session
        session['LoginStatus'] = 'Online'
        session.save()
        response = c.get("/register/", follow=True)
        self.assertRedirects(response, "/")

    def test_lost_username(self):
        c = self.client
        response = c.post('/register/',
                          {'username': '', 'password': 'test', 'confirmPassword': "test", 'phoneNumber': '1234',
                           'birthday': '123'})
        self.assertFormError(response, "registerForm", "username", "This field is required.")

    def test_lost_password(self):
        c = self.client
        response = c.post('/register/',
                          {'username': 'test', 'password': '', 'confirmPassword': "test", 'phoneNumber': '1234',
                           'birthday': '123'})
        self.assertFormError(response, "registerForm", "password", "This field is required.")

    def test_lost_confirmPassword(self):
        c = self.client
        response = c.post('/register/',
                          {'username': 'test', 'password': 'test', 'confirmPassword': "", 'phoneNumber': '1234',
                           'birthday': '123'})
        self.assertFormError(response, "registerForm", "confirmPassword", "This field is required.")

    def test_lost_phoneNumber(self):
        c = self.client
        response = c.post('/register/',
                          {'username': 'test', 'password': 'test', 'confirmPassword': "test", 'phoneNumber': '',
                           'birthday': '123'})
        self.assertFormError(response, "registerForm", "phoneNumber", "This field is required.")

    def test_lost_birthday(self):
        c = self.client
        response = c.post('/register/',
                          {'username': 'test', 'password': 'test', 'confirmPassword': "test", 'phoneNumber': '1234',
                           'birthday': ''})
        self.assertFormError(response, "registerForm", "birthday", "This field is required.")

    def test_username_existed(self):
        c = self.client
        response = c.post('/register/', {'username': 'test_customer', 'password': 'test', 'confirmPassword': "test",
                                         'phoneNumber': '1234',
                                         'birthday': '123'})
        self.assertFormError(response, 'registerForm', None, '此用户名已存在')

    def test_password_format_wrong1(self):
        c = self.client
        response = c.post('/register/', {'username': 'test', 'password': 'test', 'confirmPassword': "test",
                                         'phoneNumber': '1234',
                                         'birthday': '123'})
        self.assertFormError(response, 'registerForm', None, '密码格式不正确')

    def test_password_format_wrong2(self):
        c = self.client
        response = c.post('/register/', {'username': 'test', 'password': '123', 'confirmPassword': "123",
                                         'phoneNumber': '1234',
                                         'birthday': '123'})
        self.assertFormError(response, 'registerForm', None, '密码格式不正确')

    def test_password_format_wrong3(self):
        c = self.client
        response = c.post('/register/', {'username': 'test', 'password': 'ABC', 'confirmPassword': "ABC",
                                         'phoneNumber': '1234',
                                         'birthday': '123'})
        self.assertFormError(response, 'registerForm', None, '密码格式不正确')

    def test_confirmPassword_wrong(self):
        c = self.client
        response = c.post('/register/', {'username': 'test', 'password': 'shao0123', 'confirmPassword': "shao012",
                                         'phoneNumber': '1234',
                                         'birthday': '123'})
        self.assertFormError(response, 'registerForm', None, '两次密码不一致')

    def test_phoneNumber_format_wrong(self):
        c = self.client
        response = c.post('/register/', {'username': 'test', 'password': 'shao0123', 'confirmPassword': "shao0123",
                                         'phoneNumber': '1234',
                                         'birthday': '123'})
        self.assertFormError(response, 'registerForm', None, '电话号码长度不正确')

    def test_birthday_format_wrong(self):
        c = self.client
        response = c.post('/register/', {'username': 'test', 'password': 'shao0123', 'confirmPassword': "shao0123",
                                         'phoneNumber': '17863107810',
                                         'birthday': '123'})
        self.assertFormError(response, 'registerForm', None, '生日格式不正确')

    def test_register_successful(self):
        c = self.client
        response = c.post('/register/', {'username': 'test', 'password': 'shao0123', 'confirmPassword': "shao0123",
                                         'phoneNumber': '17863107810',
                                         'birthday': '1998/03/13'})
        self.assertRedirects(response, '/login/')
        test = Customer()
        test.username = "test"
        test.password = "shao0123"
        test.authoritySignal = False
        user = Customer.objects.get(username="test")
        self.assertRaises(ObjectDoesNotExist)
        self.assertEqual(test, user)
        test = PersonalInformation()
        test.username = 'test'
        test.phoneNumber = '17863107810'
        test.birthday = '1998/03/13'
        user = PersonalInformation.objects.get(username='test')
        self.assertRaises(ObjectDoesNotExist)
        self.assertEqual(test, user)


'''username = forms.CharField(label='用户名', widget=forms.TextInput)  # 用户名框
    password = forms.CharField(label='密码', widget=forms.PasswordInput)  # 密码框
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)
    phoneNumber = forms.CharField(label="手机号", widget=forms.TextInput)
    birthday = forms.DateField(label="生日", widget=forms.DateInput, input_formats=['%Y/%m/%d'],
                               help_text='例如：1998/03/13')'''
