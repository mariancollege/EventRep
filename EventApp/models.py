import os
import urllib
from unittest import result
from datetime import  date

import django
from django.core.files import File
from django.db import models


# Create your models here.

from EventApp import forms

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
    gender= models.CharField(max_length=20)
    profilepic=models.ImageField(upload_to='profiles/',default='none',blank=True)

    # gender = models.CharField(max_length=200)
    # photo = models.ImageField(upload_to='media/')
    # contactno = models.IntegerField(default=00)
    edate=models.DateField((date),default=date.today())
    yop = models.IntegerField(blank=True, null=True)
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.imagefile = None
    #     self.url = None

    def __str__(self):
        return self.username

    def str(self, imagefile):
        pass


class Admin(models.Model):
    eventid = models.IntegerField(primary_key=True)
    eventname = models.CharField(max_length=25)
    venue = models.TextField()
    regfee = models.IntegerField()
    tpm = models.IntegerField()
    ddepartment = models.CharField(max_length=200)
    descreption = models.TextField()
    brochure = models.ImageField()
    eventcategory=models.TextField()
    parti=models.IntegerField()
    edate=models.DateField(default=date.today())
    # doe=models.DateField(max_length=14)


class departmentn(models.Model):
    did=models.TextField(primary_key=True)
    cdept=models.CharField(max_length=200)

