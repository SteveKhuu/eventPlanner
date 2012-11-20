'''
Created on Nov 20, 2012

@author: Stephen_Khuu
'''
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def managing_class(value):
    css_class=""
    print value
    if value == True:
      css_class="test"
      
    return css_class