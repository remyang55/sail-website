from django import forms
from taggit.models import Tag

class TagForm(forms.Form):
    all_tags = Tag.objects.all()
    tag_choices = list(zip(all_tags, all_tags))

    tags = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=tag_choices,
        label=False
    )
