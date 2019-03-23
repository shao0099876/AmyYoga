from django import forms


class ChangePasswordForms(forms.Form):
    oldPassword = forms.CharField(label='旧密码', widget=forms.TextInput)
    newPassword = forms.CharField(label='新密码', widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)
