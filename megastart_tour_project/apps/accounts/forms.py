from django import forms
from django.contrib.auth.forms import UserCreationForm




class SignUpForm:
    class SignUpForm(UserCreationForm):
        username = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Username',
                   'class': 'form-styling'}))
        email = forms.EmailField(widget=forms.EmailInput(
            attrs={'placeholder': 'Email',
                   'class': 'form-styling'}))
        password1 = forms.CharField(widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                   'class': 'form-styling'}))
        password2 = forms.CharField(widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password',
                   'class': 'form-styling'}))


"""Келечекте бул файл өзгөрүш мүмкүн"""