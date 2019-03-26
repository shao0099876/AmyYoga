from django import forms
from django.forms import fields
from .models import Sex_Choices,Age_Choices

class CompleteForm(forms.Form):  #完善个人信息时提交的表单
    name = forms.CharField(label='姓名', widget=forms.TextInput) #姓名
    sex = fields.ChoiceField(label='性别',
                            choices=Sex_Choices,
                            widget=forms.Select)  # 性别

    age = fields.ChoiceField(label='年龄',
                            choices=Age_Choices,
                            widget=forms.Select)  # 年龄

    birthday = forms.CharField(label='生日', widget=forms.TextInput)  # 生日
    phoneNumber = forms.IntegerField(label='联系方式', widget=forms.TextInput) #联系方式
    profession = forms.CharField(label='职业', widget=forms.TextInput)  # 职业
    height = forms.IntegerField(label='身高', widget=forms.TextInput)  #身高
    weight = forms.IntegerField(label='体重', widget=forms.TextInput) #体重
    bust = forms.IntegerField(label='胸围', widget=forms.TextInput) #胸围
    waistline = forms.IntegerField(label='腰围', widget=forms.TextInput) #腰围
    hipline = forms.IntegerField(label='臀围', widget=forms.TextInput) #臀围
    shoulderwidth = forms.IntegerField(label='肩宽', widget=forms.TextInput) #肩宽