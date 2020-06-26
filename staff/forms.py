from django import forms
from tinymce.widgets import TinyMCE
from .models import StaffEmail

""" Used for staff to send emails to users """
class SendStaffEmailForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols':50, 'rows':30}))

    class Meta:
        model = StaffEmail
        fields = '__all__'