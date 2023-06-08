from django import template

register = template.Library()


@register.filter
def is_required(field):
    return field.field.required


@register.filter
def lookup(dictionary, key):
    return dictionary.get(key, None)
