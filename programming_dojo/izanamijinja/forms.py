from django import forms
from django.forms import ModelForm

from .models import *


class ShinRyugiForm(forms.ModelForm):
    
    class Meta:
        model = Ryugi
        fields = ['na']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
