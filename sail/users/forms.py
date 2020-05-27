from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SailUser, SailParticipant

class SailUserCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    # Additional fields, so we can create a SailParticipant along with a SailUser
    # Credits to https://stackoverflow.com/questions/7584977/in-django-how-can-i-create-a-user-and-a-user-profile-at-the-same-time-from-a-sin
    role = forms.ChoiceField(choices=SailParticipant.ROLE_CHOICES)
    year_in_school = forms.ChoiceField(choices=SailParticipant.YEAR_IN_SCHOOL_CHOICES)

    class Meta:
        model = SailUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
