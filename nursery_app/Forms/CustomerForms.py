from django import forms
from django import forms
from django.db import models
from django.db.models import fields
from django.forms.widgets import Textarea
from ..models import CustomerDetails
import re


class CustomerRegForm(forms.ModelForm):
    cust_name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'style':'width:300px','class':'form-control'}))
    cust_address=forms.CharField(label="Address",widget=forms.Textarea(attrs={'rows':'5','cols':'25','class':'form-control'}))
    cust_phno=forms.CharField(label="Phone No",widget=forms.TextInput(attrs={'style':'width:300px','class':'form-control'}))
    cust_email=forms.CharField(label="Email",widget=forms.TextInput(attrs={'style':'width:300px','class':'form-control'}))
    cust_passwd=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'style':'width:300px','class':'form-control'}))  
    cust_img=forms.ImageField(label="Upload Pic",widget=forms.FileInput(attrs={'style':'width:300px','class':'form-control'}))
    class Meta:
        model=CustomerDetails
        exclude=('cust_id',)