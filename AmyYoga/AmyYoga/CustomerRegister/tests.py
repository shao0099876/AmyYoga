from django.test import TestCase
from Database.models import *
# Create your tests here.
class CustomerRegisterTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username="test_admin", authoritySignal=True, password="test_admin_password")
        Customer.objects.create(username="test_customer", password="test_customer_password")
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
                          {'username': 'test', 'confirmPassword': "test", 'phoneNumber': '1234',
                           'birthday': '123'})
        self.assertFormError(response, "registerForm", "password", "This field is required.")
'''username = forms.CharField(label='用户名', widget=forms.TextInput)  # 用户名框
    password = forms.CharField(label='密码', widget=forms.PasswordInput)  # 密码框
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)
    phoneNumber = forms.CharField(label="手机号", widget=forms.TextInput)
    birthday = forms.DateField(label="生日", widget=forms.DateInput, input_formats=['%Y/%m/%d'],
                               help_text='例如：1998/03/13')'''