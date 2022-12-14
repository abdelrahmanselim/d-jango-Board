from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = {'username', 'first_name', 'last_name', 'password1', 'password2', 'email'}


