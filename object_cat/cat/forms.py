from django.forms import ModelForm
from .models import Cat, User
from django import forms

class Catform(ModelForm):
    class Meta:
        model = Cat
        fields = ['name','treatment','date_of_birth']

class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'password': forms.PasswordInput() 
        }

class totalUserform(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone_number', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput() 
        }

class editUserform(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone_number', 'email', 'password']

