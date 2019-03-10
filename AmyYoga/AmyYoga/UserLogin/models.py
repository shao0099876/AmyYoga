from django.db import models


# Create your models here.
class PersonalInformation(models.Model):
    phoneNumber = models.CharField(blank=False,max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField()
    profession = models.CharField(max_length=20)
    sex = models.BooleanField(default=False)


class SecurityQA(models.Model):
    securityQuestion1 = models.CharField(max_length=20)
    securityQuestion2 = models.CharField(max_length=20)
    securityQuestion3 = models.CharField(max_length=20)
    securityAnswer1 = models.TextField()
    securityAnswer2 = models.TextField()
    securityAnswer3 = models.TextField()


class Customer(models.Model):
    personalInformation = models.OneToOneField(
        PersonalInformation,
        on_delete=models.CASCADE
    )
    securityQA = models.OneToOneField(
        SecurityQA,
        on_delete=models.CASCADE
    )
    authoritySignal = models.BooleanField(default=False)
    username = models.CharField(primary_key=True,max_length=20)
    password = models.CharField(blank=False,max_length=20)
