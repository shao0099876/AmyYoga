from django.db import models


# Create your models here.

class PersonalInformation():  # 个人信息类
    phoneNumber = 0  # 电话号码

    @classmethod
    def setPhoneNumber(self, p):
        self.phoneNumber = p;


class SecurityQA():
    securityQuestion=[-1,-1,-1]
    securityAnswer=["","",""]




class Customer(models.Model):  # 用户类（管理员和客户合并到同一个类，用authoritySignal区分）
    authoritySignal = models.BooleanField(default=False)  # 身份标志，False为客户，True为管理员
    username = models.CharField(primary_key=True, max_length=20)  # 用户名
    password = models.CharField(max_length=20)  # 密码
    personalInformation = PersonalInformation()  # 个人信息

    @classmethod
    def checkAuthority(self, uncheckPassword):  # 身份认证函数，以后如果需要加入数据库内密码加密，可在该函数内添加加密解密函数
        if self.password == uncheckPassword:
            return True
        else:
            return False

    @classmethod
    def createPersonalInformation(self, phone):
        self.personalInformation.setPhoneNumber(phone)

    @classmethod
    def isAdministrator(self):
        if self.authoritySignal:
            return True
        else:
            return False
