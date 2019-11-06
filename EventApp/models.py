from datetime import  date
from django.db import models


class months(models.Model):
    mid=models.CharField(max_length=10)
    mname=models.CharField(max_length=10)


class week(models.Model):
    wid=models.CharField(max_length=10)
    wname=models.CharField(max_length=10)


class User(models.Model):
    username = models.TextField(unique=True)
    password = models.TextField()
    name = models.TextField()
    regno = models.TextField()
    collegeid = models.TextField()
    departmentid = models.TextField()
    courseid = models.TextField()
    gender = models.CharField(max_length=20)
    profilepic = models.ImageField(upload_to='profiles/',default='none',blank=True)
    contactno = models.IntegerField()
    edate = models.DateField((date),default=date.today())
    yop = models.IntegerField(blank=True, null=True)
    usertype = models.TextField(default='student')


class Admin(models.Model):
    eventid = models.IntegerField(primary_key=True)
    eventname = models.CharField(max_length=25)
    venue = models.TextField()
    regfee = models.IntegerField()
    tpm = models.IntegerField()
    ddepartment = models.CharField(max_length=200)
    descreption = models.TextField()
    brochure =  models.ImageField(upload_to='brochures/',default='none',blank=True)
    eventcategory = models.TextField()
    parti = models.IntegerField()
    edate = models.TextField()


class departmentn(models.Model):
    did=models.TextField(primary_key=True)
    cdept=models.CharField(max_length=200)

