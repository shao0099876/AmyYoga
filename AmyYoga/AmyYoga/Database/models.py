from django.db import models
from django.forms import fields


# Create your models here.


class CommonUsername(models.Model):
    username = models.CharField(primary_key=True, max_length=20)

    class Meta:
        abstract = True


class SecurityQA(CommonUsername):
    securityQ1 = models.CharField(max_length=50)
    securityA1 = models.CharField(max_length=50)
    securityQ2 = models.CharField(max_length=50)
    securityA2 = models.CharField(max_length=50)
    securityQ3 = models.CharField(max_length=50)
    securityA3 = models.CharField(max_length=50)

    def checkSecurityQA(self, Qnum, Ans):
        if self.securityQ1 == Qnum:
            if self.securityA1 == Ans:
                return True
            else:
                return False
        if self.securityQ2 == Qnum:
            if self.securityA2 == Ans:
                return True
            else:
                return False
        if self.securityQ3 == Qnum:
            if self.securityA3 == Ans:
                return True
            else:
                return False

    def getSecurityQuestion(self, p):
        if p == 1:
            return self.securityQ1
        elif p == 2:
            return self.securityQ2
        elif p == 3:
            return self.securityQ3


class Customer(CommonUsername):  # 用户类（管理员和客户合并到同一个类，用authoritySignal区分）
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

    def setPassword(self, password):
        self.password = password
        self.save()


SexChoices = (
    (False, '女'),
    (True, '男')
)  # 性别下拉列表

AgeChoices = (
    (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'),
    (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'),
    (20, '20'),
    (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'),
    (30, '30'),
    (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'),
    (40, '40'),
    (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'),
    (50, '50'),
    (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'),
    (60, '60'),
    (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'),
    (70, '70'),
    (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'),
    (80, '80'),
    (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'),
    (90, '90'),
    (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'),
    (100, '100'),
    (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), (106, '106'), (107, '107'), (108, '108'),
    (109, '109'), (110, '110')
)  # 年龄下拉列表


class PersonalInformation(CommonUsername):  # 个人信息类
    phoneNumber = models.CharField(max_length=20, default="")  # 电话号码
    name = models.CharField(max_length=20, default="")  # 客户姓名
    age = models.IntegerField(default=0, choices=AgeChoices)
    birthday = models.DateField(default='1970-01-01')
    profession = models.CharField(max_length=20)
    sex = models.BooleanField(default=False, choices=SexChoices)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    bust = models.FloatField(default=0)
    waistline = models.FloatField(default=0)
    hipline = models.FloatField(default=0)
    shoulderwidth = models.FloatField(default=0)

    def setPhoneNumber(self, p):
        self.phoneNumber = p
        self.save()

    def getPhoneNumber(self):
        return self.phoneNumber

    def setName(self, p):
        self.name = p
        self.save()

    def getName(self):
        return self.name

    def setAge(self, p):
        self.age = p
        self.save()

    def getAge(self):
        return self.age

    def setBirthday(self, p):
        self.birthday = p
        self.save()

    def getBirthday(self):
        return self.birthday

    def setProfession(self, p):
        self.profession = p
        self.save()

    def getProfession(self):
        return self.profession

    def setSex(self, p):
        self.sex = p
        self.save()

    def getSex(self):
        return self.sex

    def setHeight(self, p):
        self.height = p
        self.save()

    def getHeight(self):
        return self.height

    def setWeight(self, p):
        self.weight = p
        self.save()

    def getWeight(self):
        return self.weight

    def setBust(self, p):
        self.bust = p
        self.save()

    def getBust(self):
        return self.bust

    def setWaistline(self, p):
        self.waistline = p
        self.save()

    def getWaistline(self):
        return self.waistline

    def setHipline(self, p):
        self.hipline = p
        self.save()

    def getHipline(self):
        return self.hipline

    def setShoulderwidth(self, p):
        self.shoulderwidth = p
        self.save()

    def getShoulderwidth(self):
        return self.shoulderwidth


class Course(models.Model):  # 课程信息
    coursename = models.CharField(primary_key=True, max_length=20)  # 课程名
    courseintroduction = models.CharField(max_length=100, default="")  # 课程介绍
    courseprice = models.IntegerField(default=0)  # 课程价格
    course_flag = models.BooleanField(default=True)  # 标记课程是否在使用

    def setCourseName(self, p):
        self.coursename = p
        self.save()

    def getCourseName(self):
        return self.coursename

    def setCourseIntroduction(self, p):
        self.courseintroduction = p
        self.save()

    def getCourseIntroduction(self):
        return self.courseintroduction

    def setCoursePrice(self, p):
        self.courseprice = p
        self.save()

    def getCoursePrice(self):
        return self.courseprice

    def setCourseFlag(self, p):
        self.course_flag = p
        self.save()

    def getCourseFlag(self):
        return self.course_flag

    def create(self, a, b, c):
        self.coursename = a
        self.courseintroduction = b
        self.courseprice = c
        self.course_flag = True
        self.save()


class PhysicalAssessment(models.Model):
    number = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=20)
    date = models.DateField()
    caption = models.CharField(max_length=50)
    text = models.TextField()

    def getNumber(self):
        return self.number

    def setNumber(self, p):
        self.number = p
        self.save()

    def getCustomer(self):
        return self.customer

    def setCustomer(self, p):
        self.customer = p
        self.save()

    def getDate(self):
        return self.date

    def setDate(self, p):
        self.date = p
        self.save()

    def getCaption(self):
        return self.caption

    def setCaption(self, p):
        self.caption = p
        self.save()

    def getText(self):
        return self.text

    def setText(self, p):
        self.text = p
        self.save()


class BuyRecord(models.Model):
    number = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    coursename = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now=True)
    pay_flag = models.BooleanField(default=False)  # 标记是否付钱的订单
    valid = models.BooleanField(default=True)  # 标记是否为取消的订单

    def getNumber(self):
        return self.number

    def setNumber(self, p):
        self.number = p
        self.save()

    def getUsername(self):
        return self.username

    def setUsername(self, p):
        self.username = p
        self.save()

    def getCoursename(self):
        return self.coursename

    def setCoursename(self, p):
        self.coursename = p
        self.save()

    def getAmount(self):
        return self.amount

    def setAmount(self, p):
        self.amount = p
        self.save()

    def getTime(self):
        return self.time

    def setTime(self, p):
        self.time = p
        self.save()

    def getPayFlag(self):
        return self.pay_flag

    def setPayFlag(self, p):
        self.pay_flag = p
        self.save()

    def getValid(self):
        return self.valid

    def setValid(self, p):
        self.valid = p
        self.save()
