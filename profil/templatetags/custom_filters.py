from django import template

register = template.Library()

@register.filter
def splitlines(value):
    """Pisahkan string berdasarkan baris menjadi list."""
    if not isinstance(value, str):
        return []
    return value.strip().splitlines()
