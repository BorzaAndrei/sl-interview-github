from django import template


register = template.Library()


@register.filter
def sanitize_names(value):
    return value.replace('--', '.')