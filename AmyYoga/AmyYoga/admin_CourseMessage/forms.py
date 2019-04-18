from django import forms
from Database import models

class AddCourseForm(forms.Form):  #增加课程的表单
    coursename = forms.CharField(label='课程名', widget=forms.TextInput)  # 课程名框
    courseintroduction = forms.CharField(label='课程介绍', widget=forms.TextInput)  # 课程介绍框架
    courseprice = forms.IntegerField(label='课程价格')  # 课程价格框

class ModCourseForm(forms.ModelForm):  #修改课程的表单
    class Meta:
        model = models.Course
        exclude = [ 'coursename' ,'course_flag']
        labels = {
            'courseintroduction': '课程介绍',
            'courseprice': '价格',
        }
        help_texts ={
            'courseprice': '请输入正整数'
        }
        error_messages = {
            '_all_':{
                'required':'请输入内容',
                'invaild':'请检查输入的内容'
            }
        }
