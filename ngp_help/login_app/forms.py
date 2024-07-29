from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password', max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Confirm Password', max_length=30, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
