from django import template

register = template.Library()

# Credits to https://stackoverflow.com/questions/2047622/how-to-paginate-django-with-other-get-variables

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
