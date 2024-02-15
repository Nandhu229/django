from django.db import models
from django.utils import timezone

# Create your models here.

class login(models.Model):
    userid = models.CharField(max_length=200)
    password = models.IntegerField()
class RegisterModel(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=200)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mobilenum=models.BigIntegerField()
    email=models.EmailField(max_length=400,null=True)

class hospital_details(models.Model):
    Patient_Name=models.CharField(max_length=300)
    Doctor_Name=models.CharField(max_length=300)
    Patient_id=models.IntegerField()
    Patient_Data=models.FileField()
    Admit_date=models.DateField(default=timezone.now)
    Discharge_date=models.DateField(null=True)



