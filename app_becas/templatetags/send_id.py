from django import template
from app_becas.models import Calendar
import urllib
from django.shortcuts import redirect


register = template.Library()

@register.simple_tag(name="send_id")
def send_id(value):
    mydata = Calendar.objects.filter(auto_id=value)
    
    your_params = {
        'calendar' : mydata,
    }
    return redirect_params('calendar_show_info', str(value))

def redirect_params(url, params):
    response = redirect(url)
    if params:
        query_string = "auto_id="+params
        response['Location'] += '?' + query_string

    print(response)
    return response.url