import os
import urllib
from unittest import result

from django.core.files import File
from django.db import models


# Create your models here.
from EventApp import forms


class User(models.Model):
    username = models.TextField(unique=True)
    password = models.TextField()
    name = models.TextField()
    regno = models.TextField()
    collegeid = models.TextField()
    departmentid = models.TextField()
    courseid = models.TextField()
    # gender = models.CharField(max_length=200)
    # photo = models.ImageField(upload_to='media/')
    contactno = models.IntegerField()
    yop = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imagefile = None
        self.url = None

    def cache(self):
        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                os.path.basename(self.url),
                File(open(result[0], 'rb'))
                )
            self.save()

    def __str__(self):
        return self.username

    def __str__(self):
        return self.str(self.imagefile)

    def str(self, imagefile):
        pass


class Admin(models.Model):
    eventid = models.TextField(primary_key=True)
    eventname = models.CharField(max_length=25)
    venue = models.TextField()
    date = models.DateField()
    regfee = models.IntegerField()
    tpm = models.IntegerField()
    department = models.TextField()
    descreption = models.TextField()
    brochure = models.ImageField()

class User2(models.Model):
    username2 = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    eventname = models.CharField(max_length=25)
