from django import forms
from Database.models import Customer
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class LoginForm(forms.Form):  # 登录时输入的表单
    username = forms.CharField(label='用户名', widget=forms.TextInput)  # 用户名框
    password = forms.CharField(label='密码', widget=forms.PasswordInput)  # 密码框
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        try:
            user = Customer.objects.get(username=username)  # 尝试查询该用户
        except ObjectDoesNotExist:
            raise ValidationError("用户名不存在")
        if not user.checkAuthority(password):
            raise ValidationError("密码错误")  # 返回密码错误信息
        return cleaned_data
