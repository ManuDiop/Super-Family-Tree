from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput,label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class LogoutForm(forms.Form):
    pass