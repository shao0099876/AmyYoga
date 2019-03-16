from django import forms


class RegisterForm(forms.Form):  # 登录时输入的表单
    username = forms.CharField(label='用户名', widget=forms.TextInput)  # 用户名框
    password = forms.CharField(label='密码', widget=forms.PasswordInput)  # 密码框
    confirmPassword=forms.CharField(label="确认密码",widget=forms.PasswordInput)
    phoneNumber=forms.CharField(label="手机号",widget=forms.TextInput)
