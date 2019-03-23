from django.db import models
from Interface import Interface


# Create your models here.


class SecurityQA():
    securityQuestion = [-1, -1, -1]
    securityAnswer = ["", "", ""]


class PersonalInformation(models.Model, Interface.PersonalInformationInterface):  # 个人信息类
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

    def getPhoneNumber(self):
        return self.phoneNumber

    def setName(self, p):
        self.name = p

    def getName(self):
        return self.name

    def setAge(self, p):
        self.age = p

    def getAge(self):
        return self.age

    def setBirthday(self, p):
        self.birthday = p

    def getBirthday(self):
        return self.birthday

    def setProfession(self, p):
        self.Profession = p

    def getProfession(self):
        return self.profession

    def setSex(self, p):
        self.sex = p

    def getSex(self):
        return self.sex

    def setHeight(self, p):
        self.height = p

    def getHeight(self):
        return self.height

    def setWeight(self, p):
        self.weight = p

    def getWeight(self):
        return self.weight

    def setBust(self, p):
        self.bust = p

    def getBust(self):
        return self.bust

    def setWaistline(self, p):
        self.waistline = p

    def getWaistline(self):
        return self.waistline

    def setHipline(self, p):
        self.hipline = p

    def getHipline(self):
        return self.hipline

    def setShoulderwidth(self, p):
        self.shoulderwidth = p

    def getShoulderwidth(self):
        return self.shoulderwidth


class Customer(models.Model, Interface.CustomerInterface):  # 用户类（管理员和客户合并到同一个类，用authoritySignal区分）
    authoritySignal = models.BooleanField(default=False)  # 身份标志，False为客户，True为管理员
    username = models.CharField(primary_key=True, max_length=20)  #
    personalInformation = models.OneToOneField(PersonalInformation,on_delete=models.CASCADE)  # 个人信息

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

    def setPhoneNumber(self, p):
        self.personalInformation.setPhoneNumber(p)

    def getPhoneNumber(self):
        return self.personalInformation.getPhoneNumber()

    def setName(self, p):
        self.personalInformation.setName(p)

    def getName(self):
        return self.personalInformation.getName()

    def setAge(self, p):
        self.personalInformation.setAge(p)

    def getAge(self):
        return self.personalInformation.getAge()

    def setBirthday(self, p):
        self.personalInformation.setBirthday(p)

    def getBirthday(self):
        return self.personalInformation.getBirthday()

    def setProfession(self, p):
        self.personalInformation.setProfession(p)

    def getProfession(self):
        return self.personalInformation.getProfession()

    def setSex(self, p):
        self.personalInformation.setSex(p)

    def getSex(self):
        return self.personalInformation.getSex()

    def setHeight(self, p):
        self.personalInformation.setHeight(p)

    def getHeight(self):
        return self.personalInformation.getHeight()

    def setWeight(self, p):
        self.personalInformation.setWeight(p)

    def getWeight(self):
        return self.personalInformation.getWeight()

    def setBust(self, p):
        self.personalInformation.setBust(p)

    def getBust(self):
        return self.personalInformation.getBust()

    def setWaistline(self, p):
        self.personalInformation.setWaistline(p)

    def getWaistline(self):
        return self.personalInformation.getWaistline()

    def setHipline(self, p):
        self.personalInformation.setHipline(p)

    def getHipline(self):
        return self.personalInformation.getHipline()

    def setShoulderwidth(self, p):
        self.personalInformation.setShoulderwidth(p)

    def getShoulderwidth(self):
        return self.personalInformation.getShoulderwidth()

    def create(self, username, password, phoneNumber, birthday):
        self.username = username
        self.password = password
        PersonalInformation.objects.create
        self.personalInformation.setPhoneNumber(phoneNumber)
        self.personalInformation.setBirthday(birthday)
        self.save()
