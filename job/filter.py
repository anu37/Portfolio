from django import template
from django.contrib.auth.models import Group


register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)

    
@register.filter(name='transtimes') 
def transtimes(number):
    return range(5-number)