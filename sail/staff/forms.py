from django import forms
from tinymce.widgets import TinyMCE
from .models import Email

class SendEmailForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols':50, 'rows':30}))

    class Meta:
        model = Email
        fields = '__all__'