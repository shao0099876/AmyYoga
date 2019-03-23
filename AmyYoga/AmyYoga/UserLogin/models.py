from django.db import models
from Interface import Interface


# Create your models here.


class SecurityQA():
    securityQuestion = [-1, -1, -1]
    securityAnswer = ["", "", ""]


class Customer(models.Model, Interface.CustomerInterface):  # 用户类（管理员和客户合并到同一个类，用authoritySignal区分）
    authoritySignal = models.BooleanField(default=False)  # 身份标志，False为客户，True为管理员
    username = models.CharField(primary_key=True, max_length=20)  # 用户名
    password = models.CharField(max_length=20)  # 密码

    class __PersonalInformation(Interface.PersonalInformationInterface):  # 个人信息类
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

        def setPhoneNumber(self, p):
            self.__phoneNumber = p

        def getPhoneNumber(cls):
            return cls.__phoneNumber

        def setName(self, p):
            self.__name = p

        def getName(cls):
            return cls.__name

        def setAge(self, p):
            self.__age = p

        def getAge(cls):
            return cls.__age

        def setBirthday(self, p):
            self.__birthday = p

        def getBirthday(cls):
            return cls.__birthday

        def setProfession(self, p):
            self.__Profession = p

        def getProfession(cls):
            return cls.__profession

        def setSex(self, p):
            self.__sex = p

        def getSex(cls):
            return cls.__sex

        def setHeight(cls, p):
            cls.__height = p

        def getHeight(cls):
            return cls.__height

        def setWeight(cls, p):
            cls.__weight = p

        def getWeight(cls):
            return cls.__weight

        def setBust(cls, p):
            cls.__bust = p

        def getBust(cls):
            return cls.__bust

        def setWaistline(cls, p):
            cls.__waistline = p

        def getWaistline(cls):
            return cls.__waistline

        def setHipline(cls, p):
            cls.__hipline = p

        def getHipline(cls):
            return cls.__hipline

        def setShoulderwidth(cls, p):
            cls.__shoulderwidth = p

        def getShoulderwidth(cls):
            return cls.__shoulderwidth

    __personalInformation = __PersonalInformation()  # 个人信息

    def checkAuthority(self, uncheckPassword):  # 身份认证函数，以后如果需要加入数据库内密码加密，可在该函数内添加加密解密函数
        if self.password == uncheckPassword:
            return True
        else:
            return False

    def createPersonalInformation(self, phone):
        self.personalInformation.setPhoneNumber(phone)

    def isAdministrator(self):
        if self.authoritySignal:
            return True
        else:
            return False

    def setPhoneNumber(self, p):
        personalInformation.setPhoneNumber(p)

    def getPhoneNumber(cls):
        return personalInformation.getPhoneNumber()

    def setName(self, p):
        personalInformation.setName(p)

    def getName(cls):
        return personalInformation.getName()

    def setAge(self, p):
        personalInformation.setAge(p)

    def getAge(cls):
        return personalInformation.getAge()

    def setBirthday(self, p):
        personalInformation.setBirthday(p)

    def getBirthday(cls):
        return personalInformation.getBirthday()

    def setProfession(self, p):
        personalInformation.setProfession(p)

    def getProfession(cls):
        return personalInformation.getProfession()

    def setSex(self, p):
        personalInformation.setSex(p)

    def getSex(cls):
        return personalInformation.getSex()

    def setHeight(cls, p):
        personalInformation.setHeight(p)

    def getHeight(cls):
        return personalInformation.getHeight()

    def setWeight(cls, p):
        personalInformation.setWeight(p)

    def getWeight(cls):
        return personalInformation.getWeight()

    def setBust(cls, p):
        personalInformation.setBust(p)

    def getBust(cls):
        return personalInformation.getBust()

    def setWaistline(cls, p):
        personalInformation.setWaistline(p)

    def getWaistline(cls):
        return personalInformation.getWaistline()

    def setHipline(cls, p):
        personalInformation.setHipline(p)

    def getHipline(cls):
        return personalInformation.getHipline()

    def setShoulderwidth(cls, p):
        personalInformation.setShoulderwidth(p)

    def getShoulderwidth(cls):
        return personalInformation.getShoulderwidth()
