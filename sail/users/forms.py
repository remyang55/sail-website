from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SailUser

class SailUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField()

    class Meta:
        model = SailUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
