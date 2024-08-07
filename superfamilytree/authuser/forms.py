from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)