from django import forms
from Tools.Const import SECURITY_QUESTION_LIST

class RegisterForm(forms.Form):  # 登录时输入的表单
    username = forms.CharField(label='用户名', widget=forms.TextInput)  # 用户名框
    password = forms.CharField(label='密码', widget=forms.PasswordInput)  # 密码框
    confirmPassword=forms.CharField(label="确认密码",widget=forms.PasswordInput)
    phoneNumber=forms.CharField(label="手机号",widget=forms.TextInput)
    birthday=forms.DateField(label="生日",widget=forms.DateInput,input_formats=['%m/%d'],help_text='mm/dd')
    #securityQuestion1=forms.ChoiceField(label="密保问题1",choices=((0,SECURITY_QUESTION_LIST[0]),(1,SECURITY_QUESTION_LIST[1]),(2,SECURITY_QUESTION_LIST[2])))
