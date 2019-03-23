from django.db import models
from Interface import Interface


# Create your models here.


class SecurityQA():
    securityQuestion = [-1, -1, -1]
    securityAnswer = ["", "", ""]

class CommonUsername(models.Model):
    username=models.CharField(primary_key=True,max_length=20)

    class Meta:
        abstract=True

class Customer(CommonUsername,Interface.CustomerInterface):  # 用户类（管理员和客户合并到同一个类，用authoritySignal区分）
    authoritySignal = models.BooleanField(default=False)  # 身份标志，False为客户，True为管理员
    password = models.CharField(max_length=20)  # 密码

    def checkAuthority(self, uncheckPassword):  # 身份认证函数，以后如果需要加入数据库内密码加密，可在该函数内添加加密解密函数
        if self.password == uncheckPassword:
            return True
        else:
            return False

    def isAdministrator(self):
        if self.authoritySignal:
            return True
        else:
            return False

class PersonalInformation(CommonUsername,Interface.PersonalInformationInterface):  # 个人信息类
    phoneNumber = models.CharField(max_length=20)  # 电话号码
    name = models.CharField(max_length=20)  # 客户姓名
    age = models.IntegerField()
    birthday = models.DateField()
    profession = models.CharField(max_length=20)
    sex = models.BooleanField()
    height = models.FloatField()
    weight = models.FloatField()
    bust = models.FloatField()
    waistline = models.FloatField()
    hipline = models.FloatField()
    shoulderwidth = models.FloatField()

    def setPhoneNumber(self, p):
        self.phoneNumber = p
        self.objects.save()

    def getPhoneNumber(self):
        return self.phoneNumber

    def setName(self, p):
        self.name = p
        self.objects.save()

    def getName(self):
        return self.name

    def setAge(self, p):
        self.age = p
        self.objects.save()

    def getAge(self):
        return self.age

    def setBirthday(self, p):
        self.birthday = p
        self.objects.save()

    def getBirthday(self):
        return self.birthday

    def setProfession(self, p):
        self.Profession = p
        self.objects.save()

    def getProfession(self):
        return self.profession

    def setSex(self, p):
        self.sex = p
        self.objects.save()

    def getSex(self):
        return self.sex

    def setHeight(self, p):
        self.height = p
        self.objects.save()

    def getHeight(self):
        return self.height

    def setWeight(self, p):
        self.weight = p
        self.objects.save()

    def getWeight(self):
        return self.weight

    def setBust(self, p):
        self.bust = p
        self.objects.save()

    def getBust(self):
        return self.bust

    def setWaistline(self, p):
        self.waistline = p
        self.objects.save()

    def getWaistline(self):
        return self.waistline

    def setHipline(self, p):
        self.hipline = p
        self.objects.save()

    def getHipline(self):
        return self.hipline

    def setShoulderwidth(self, p):
        self.shoulderwidth = p
        self.objects.save()

    def getShoulderwidth(self):
        return self.shoulderwidth

