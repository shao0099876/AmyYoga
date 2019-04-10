from django import forms
from Database.models import Customer
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import time


class RegisterForm(forms.Form):  # 登录时输入的表单
    username = forms.CharField(label='用户名', widget=forms.TextInput)  # 用户名框
    password = forms.CharField(label='密码', widget=forms.PasswordInput)  # 密码框
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)
    phoneNumber = forms.CharField(label="手机号", widget=forms.TextInput)
    birthday = forms.DateField(label="生日", widget=forms.DateInput, input_formats=['%Y/%m/%d'],
                               help_text='例如：1998/03/13')

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        user = Customer()  # 创建空用户对象
        flag = True
        try:
            user = Customer.objects.get(username=username)  # 尝试查询该用户
        except ObjectDoesNotExist:  # 用户名不存在，执行创建操作
            flag = False
        if flag:
            raise ValidationError("此用户名已存在")

        password = cleaned_data.get('password')
        smallCharacter = 0
        bigCharacter = 0
        number = 0
        for c in password:
            if c >= 'a' and c <= 'z':
                smallCharacter = 1
            elif c >= 'A' and c <= 'Z':
                bigCharacter = 1
            elif c >= '0' and c <= '9':
                number = 1
        res = smallCharacter + bigCharacter + number
        if res < 2:
            raise ValidationError("密码格式不正确")

        confirmpassword = cleaned_data.get("confirmPassword")
        if password != confirmpassword:
            raise ValidationError("两次密码不一致")

        phonenumber = cleaned_data.get("phoneNumber")
        if len(phonenumber) != 11:
            raise ValidationError("电话号码长度不正确")

        birthday = cleaned_data.get("birthday")
        if birthday is None:
            raise ValidationError("生日格式不正确")
