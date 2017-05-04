from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email','type':'email'}), label='')
    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'}), label='')
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'password'}), label='')
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'reapeat password'}), label='')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )