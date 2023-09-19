from django import template
from app.models import *

register = template.Library()


@register.simple_tag(name='my_red_line',
                     takes_context=True)
def my_tag(context, str_: str):
    return f'{str_} This is my tag\n' \
           f'{context["data"]}'


@register.inclusion_tag('app/inc.html')
def products():
    product_list = Product.objects.all()
    return {'product_list': product_list}


@register.filter
def no_letter(value, letter):
    return value.replace(letter, '')
