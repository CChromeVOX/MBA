from django.forms import ModelForm
from django import forms
from .models import *
class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [ 'comment', 'lesson']
