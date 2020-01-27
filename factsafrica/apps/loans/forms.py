from .models import Customer
from django import forms
from django.db import models

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')