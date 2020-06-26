from django import forms
from taggit.models import Tag

import datetime

# Important note: For each tuple in CHOICES for these filters, the two values must be the same!
# This is so that the form could fill its initial values from the query parameters in the URL

""" Multiple checkbox form that is used to filter courses displayed on CourseListView, based on the selected tags """
class TagForm(forms.Form):

    # Database queries in forms cannot be done at import time, or initial migrations will fail!
    # Solution is to move queries into __init__()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        all_tags = Tag.objects.all()
        self.fields['tags'].choices = list(zip(all_tags, all_tags))

    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'onchange':'form.submit();'}),
        choices=[('' , '')],
        label=False
    )

""" Multiple checkbox form that is used to filter courses displayed on CourseListView, based on the selected starting times """
class TimeForm(forms.Form):
    course_times = [datetime.datetime(2020, 4, 4, 10) + k*datetime.timedelta(hours=1) for k in range(6)]
    time_choices = [(time.strftime("%H:%M"), time.strftime("%H:%M")) for time in course_times]

    times = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'onchange':'form.submit();'}),
        choices=time_choices,
        label=False
    )
