from django import template
register = template.Library()
import decimal

@register.filter
def to_decimal(a, *args, **kwargs):
    # you would need to do any localization of the result here
    if isinstance(a, str):
        a = a.replace(',', '.')
    return decimal.Decimal(a)