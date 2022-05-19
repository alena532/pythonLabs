from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email','username','passport_numer', 'passport_series', 'age']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
