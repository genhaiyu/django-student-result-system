from cryptography.fernet import Fernet
from django import template
from django.conf import settings

register = template.Library()


@register.filter
def replaceBlank(value, string=""):
    value = str(value).replace(string, '')
    return value


@register.filter
def encryptdata(value):
    fernet = Fernet(settings.ID_ENCRYPTION_KEY)
    value = fernet.encrypt(str(value).encode())
    return value
