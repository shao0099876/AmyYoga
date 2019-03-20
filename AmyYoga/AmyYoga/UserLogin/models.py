from django.db import models


# Create your models here.

class PersonalInformation():  # 个人信息类
    __phoneNumber = 0  # 电话号码
    __name = ""  # 客户姓名
    __age = 0  # 年龄
    __birthday = None  # 生日
    __profession = None  # 职业
    __sex = None  # 性别
    __height = 0  # 身高
    __weight = 0  # 体重
    __bust = 0  # 胸围
    __waistline = 0  # 腰围
    __hipline = 0  # 臀围
    __shoulderwidth = 0  # 肩宽

    @classmethod
    def setPhoneNumber(self, p):
        self.__phoneNumber = p;

    @classmethod
    def getPhoneNumber(cls):
        return cls.__phoneNumber

    @classmethod
    def setName(self, p):
        self.__name = p

    @classmethod
    def getName(cls):
        return cls.__name

    @classmethod
    def setAge(self, p):
        self.__age = p

    @classmethod
    def getAge(cls):
        return cls.__age

    @classmethod
    def setBirthday(self, p):
        self.__birthday = p

    @classmethod
    def getBirthday(cls):
        return cls.__birthday

    @classmethod
    def setProfession(self, p):
        self.__Profession = p

    @classmethod
    def getProfession(cls):
        return cls.__profession

    @classmethod
    def setSex(self, p):
        self.__sex = p

    @classmethod
    def getSex(cls):
        return cls.__sex

    @classmethod
    def setHeight(cls, p):
        cls.__height = p

    @classmethod
    def getHeight(cls):
        return cls.__height

    @classmethod
    def setWeight(cls, p):
        cls.__weight = p

    @classmethod
    def getWeight(cls):
        return cls.__weight

    @classmethod
    def setBust(cls, p):
        cls.__bust = p

    @classmethod
    def getBust(cls):
        return cls.__bust

    @classmethod
    def setWaistline(cls, p):
        cls.__waistline = p

    @classmethod
    def getWaistline(cls):
        return cls.__waistline

    @classmethod
    def setHipline(cls, p):
        cls.__hipline = p

    @classmethod
    def getHipline(cls):
        return cls.__hipline

    @classmethod
    def setShoulderwidth(cls, p):
        cls.__shoulderwidth = p

    @classmethod
    def getShoulderwidth(cls):
        return cls.__shoulderwidth


class SecurityQA():
    securityQuestion = [-1, -1, -1]
    securityAnswer = ["", "", ""]


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
