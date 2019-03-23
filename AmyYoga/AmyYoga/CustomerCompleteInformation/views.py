from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from UserLogin.models import Customer as CustomerDB
from .forms import CompleteForm

# Create your views here.
def completeinformation(request):#用户点击提交完善的个人信息
    if request.method == 'POST':  # 如果请求为表单提交
        completeForm = CompleteForm(request.POST)  # 获取表单内容
        if completeForm.is_valid():  # 解析表单
            phoneNumber = completeForm.cleaned_data['phoneNumber']  # 联系方式
            sex = completeForm.cleaned_data['sex']  # 性别
            birthday = completeForm.cleaned_data['birthday']  # 生日
            height = completeForm.cleaned_data['height']  # 身高
            weight = completeForm.cleaned_data['weight']  # 体重
            chestline = completeForm.cleaned_data['chestline']  # 胸围
            waistline = completeForm.cleaned_data['waistline']  # 腰围
            hipline = completeForm.cleaned_data['hipline']  # 臀围
            omosline = completeForm.cleaned_data['omosline']  # 肩宽



    return render(request, 'completeinformationUI.html', locals())  # 渲染页面

def getUsername(request):
    name_of_user=request.session['username']
    return render(name_of_user, 'completeinformationUI.html', locals())  # 传递用户名


