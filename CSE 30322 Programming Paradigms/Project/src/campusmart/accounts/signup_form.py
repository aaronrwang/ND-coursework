# login_form.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Using Django's Deault Login
class CreateNewUserProfile(UserCreationForm):
    
    firstname = forms.CharField(max_length=50, required=True, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}))
    lastname = forms.CharField(max_length=50, required=True, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}))
    email = forms.CharField(max_length=50, required=True, label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))

    username = forms.CharField(
        label="Username",
        help_text='', 
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Choose a password'}),
        help_text='',
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        help_text=''
    )

    # declare what fields should be used in the form
    class Meta:
        model = User
        fields = ('firstname','lastname', 'email', 'username', 'password1', 'password2')
    
