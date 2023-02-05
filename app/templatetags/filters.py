from datetime import datetime

from django import template

register = template.Library()


@register.filter
def date_filter(arg):
    return ""

