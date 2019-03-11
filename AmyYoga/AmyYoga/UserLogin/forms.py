from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput)
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
