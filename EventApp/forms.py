from django import forms
from .models import *

gchoice=[
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
]

# class Users(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=["imagefile"]


class ModelForm:
    pass