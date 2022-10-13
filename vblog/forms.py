from django import forms
from .models import *
class postform(forms.ModelForm):
    class Meta:
        model=post
        fields="__all__"