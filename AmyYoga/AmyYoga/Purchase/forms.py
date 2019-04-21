from django import forms
from Database import models
from django.core.exceptions import ObjectDoesNotExist, ValidationError
class CourseForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput)
    coursename = forms.CharField(label='课程名', widget=forms.TextInput)
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        try:
            user = models.Customer.objects.get(username=username)  # 尝试查询该用户
        except ObjectDoesNotExist:
            raise ValidationError("用户名不存在")
        coursename = cleaned_data.get("coursename")
        try:
            course = models.Course.objects.get(coursename=coursename)  # 尝试查询该用户
        except ObjectDoesNotExist:
            raise ValidationError("课程不存在")
        return cleaned_data

class CoruseModelForm(forms.ModelForm):
    class Meta:
        model = models.BuyRecord
        exclude = [ 'time','valid']
        labels = {
            'number':'订单号',
            'username':'用户名',
            'coursename':'课程名',
            'amount':'金额',
            'pay_flag':'支付状态'
        }
