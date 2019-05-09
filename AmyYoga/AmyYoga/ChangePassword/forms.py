from django import forms
from Database.models import Customer
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class ChangePasswordForm(forms.Form):
    oldPassword = forms.CharField(label='旧密码', widget=forms.PasswordInput)
    newPassword = forms.CharField(label='新密码', widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)
    username=""
    def clean(self):
        cleaned_data = super().clean()
        oldPassword = cleaned_data.get('oldPassword')
        if oldPassword is None:
            raise ValidationError('This field is required.')
        user = Customer.objects.get(username=self.username)
        if not user.checkAuthority(oldPassword):
            raise ValidationError("密码不正确")

        newPassword = cleaned_data.get("newPassword")
        if newPassword is None:
            raise ValidationError('This field is required.')
        smallCharacter = 0
        bigCharacter = 0
        number = 0
        for c in newPassword:
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
        if newPassword != confirmpassword:
            raise ValidationError("两次密码不一致")


class ForgetPasswordForm(forms.Form):
    newPassword = forms.CharField(label='新密码', widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        newPassword = cleaned_data.get("newPassword")
        if newPassword is None:
            raise ValidationError('This field is required.')
        smallCharacter = 0
        bigCharacter = 0
        number = 0
        for c in newPassword:
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
        if newPassword != confirmpassword:
            raise ValidationError("两次密码不一致")


class UsernameForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput)

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        try:
            user = Customer.objects.get(username=username)
        except ObjectDoesNotExist:
            raise ValidationError("用户名不存在")
