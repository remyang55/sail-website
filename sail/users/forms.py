from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SailUser, SailTeacher, SailStudent

class SailUserCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = SailUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class SailTeacherCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SailTeacherCreationForm, self).__init__(*args, **kwargs)  
        self.fields['major'] = forms.CharField(max_length=SailTeacher.MAJOR_MAX_LENGTH)
        self.fields['year_in_school'] = forms.ChoiceField(choices=SailTeacher.YEAR_IN_SCHOOL_CHOICES)

    class Meta:
        model = SailTeacher
        fields = ['major', 'year_in_school']
        exclude = ('user',)

class SailStudentCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SailStudentCreationForm, self).__init__(*args, **kwargs)  
        self.fields['admitted_student'] = forms.BooleanField(required=False)
        self.fields['year_in_school'] = forms.ChoiceField(choices=SailStudent.YEAR_IN_SCHOOL_CHOICES)

    class Meta:
        model = SailStudent
        fields = ['year_in_school', 'admitted_student']
        exclude = ('user',)

class SailUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = SailUser
        fields = ['email', 'first_name', 'last_name']
