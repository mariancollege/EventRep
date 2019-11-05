from django import forms
from .models import *
# from .models import Post

gchoice=[
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
]


# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ('title', 'text',)
class ModelForm:
    pass