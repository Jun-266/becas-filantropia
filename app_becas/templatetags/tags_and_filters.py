from django import template
from django.shortcuts import redirect


register = template.Library()

@register.filter
def shorten(value, length):
    if len(value) > length:
        result = value[:length] + '...'
        return result
    return value

@register.simple_tag(name="send_id")
def send_id(my_url, value):
    
    return redirect_params(my_url, str(value))

def redirect_params(url, params):
    response = redirect(url)
    if params:
        query_string = "auto_id="+params
        response['Location'] += '?' + query_string

    return response.url

