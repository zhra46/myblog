from django.template import Library
register = Library()
import mistune
@register.filter
def toStr(value):
    return str(value)
@register.filter
def md(value):

    return mistune.markdown(value)
@register.filter
def rvs(value):
    value.reverse()
    return value