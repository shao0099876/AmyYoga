from django import forms


class ChangePasswordForm(forms.Form):
    oldPassword = forms.CharField(label='旧密码', widget=forms.TextInput)
    newPassword = forms.CharField(label='新密码', widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)


class ForgetPasswordForm(forms.Form):
    #securityQuestion=forms.CharField(label='密保问题',widget=forms.HiddenInput)
    #securityAnswer=forms.CharField(label='密保答案',widget=forms.TextInput)
    newPassword = forms.CharField(label='新密码', widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)

class UsernameForm(forms.Form):
    username=forms.CharField(label='用户名',widget=forms.TextInput)