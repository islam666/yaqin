from django import template
import os

register = template.Library()

@register.filter
def basename(value):
    return os.path.splitext(os.path.basename(value))[0]
