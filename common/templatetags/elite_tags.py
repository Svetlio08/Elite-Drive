from django import template

register = template.Library()

@register.filter
def format_price(value):
    try:
        return f"{float(value):,.2f}"
    except (TypeError, ValueError):
        return value