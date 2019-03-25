from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CompleteForm
from UserLogin.models import Customer as CustomerDB
from UserLogin.models import PersonalInformation as PersonalInformationDB
from Tools import SessionManager,FormsManager

# Create your views here.
def completeinformation(request):#用户点击提交完善的个人信息
    if request.method == 'POST':  # 如果请求为表单提交
        completeForm = CompleteForm(request.POST)  # 获取表单内容
        if completeForm.is_valid():  # 解析表单
            name = completeForm.cleaned_data['name']  # 姓名
            age = completeForm.cleaned_data['age']  # 年龄
            profession = completeForm.cleaned_data['profession']  # 职业
            phoneNumber = completeForm.cleaned_data['phoneNumber']  # 联系方式
            sex = completeForm.cleaned_data['sex']  # 性别
            birthday = completeForm.cleaned_data['birthday']  # 生日
            height = completeForm.cleaned_data['height']  # 身高
            weight = completeForm.cleaned_data['weight']  # 体重
            bust = completeForm.cleaned_data['bust']  # 胸围
            waistline = completeForm.cleaned_data['waistline']  # 腰围
            hipline = completeForm.cleaned_data['hipline']  # 臀围
            shoulderwidth = completeForm.cleaned_data['shoulderwidth']  # 肩宽

            #判断数据是否正确

            #正确过后写数据库
            name_of_user = request.session.get('username', default=None) #获取用户名
            personalInformation = PersonalInformationDB.objects.get(username=name_of_user)

            personalInformation.setName(name)
            personalInformation.setAge(age)
            personalInformation.setProfession(profession)
            personalInformation.setPhoneNumber(phoneNumber)
            personalInformation.setSex(sex)
            personalInformation.setBirthday(birthday)
            personalInformation.setHeight(height)
            personalInformation.setWeight(weight)
            personalInformation.setBust(bust)
            personalInformation.setWaistline(waistline)
            personalInformation.setHipline(hipline)
            personalInformation.setShoulderwidth(shoulderwidth)

            return HttpResponse("successed")  # 修改成功，并且留在本页面

    else:
        completeForm = CompleteForm()  # 创建表单
    return render(request, 'completeinformationUI.html', locals())  # 渲染页面

def getUsername(request):
    name_of_user=request.session.get('username',default=None)
    return render(request, 'completeinformationUI.html', locals())  # 传递用户名


