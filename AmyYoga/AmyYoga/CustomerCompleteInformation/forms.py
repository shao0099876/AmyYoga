from django import forms

class CompleteForm(forms.Form):  #完善个人信息时提交的表单
    phoneNumber=forms.CharField(label='联系方式',widget=forms.TextInput)#联系方式
    sex=forms.CharField(label='性别',widget=forms.TextInput)#性别
    birthday=forms.CharField(label='生日',widget=forms.TextInput)#生日
    height=forms.CharField(label='身高',widget=forms.TextInput) #身高
    weight=forms.CharField(label='体重',widget=forms.TextInput)#体重
    chestline=forms.CharField(label='胸围',widget=forms.TextInput)#胸围
    waistline=forms.CharField(label='腰围',widget=forms.TextInput)#腰围
    hipline=forms.CharField(label='臀围',widget=forms.TextInput)#臀围
    omosline=forms.CharField(label='肩宽',widget=forms.TextInput)#肩宽