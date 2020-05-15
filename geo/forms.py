# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User
from . import models



class PhotoForm(forms.Form):
    author = forms.ModelChoiceField(User.objects.all(), required=False)
    city = forms.ModelChoiceField(models.City.objects.all(), label='City', required=True)
    image = forms.FileField(label='Photo', required=True)
    desc = forms.CharField(label='Description',
                           widget=forms.Textarea(attrs={'placeholder': 'Description'}), required=False)