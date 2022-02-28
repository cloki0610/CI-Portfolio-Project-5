""" Custom template tag for cart app """
from django import template


register = template.Library()


@register.filter(name='calc_price')
def calc_price(price, quantity):
    """ return total price of the item """
    return price * quantity
