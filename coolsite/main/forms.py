from django.forms import ModelForm, Select, Textarea
from django import forms
from .models import *


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['lesson', 'comment']
        widgets ={
            'lesson': Select(),
            'comment': Textarea(
                attrs={
                    'rows':'2',
                    'class': 'form-control',
                    'placeholder': 'Комментарии',
                    }),
        }
