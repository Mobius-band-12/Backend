from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def validate_domain(value):
    '''Функция-валидатор для проверки корпоративного домена @lenta.ru.'''
    error_msg = 'Используйте почтовый адрес на домене @lenta.ru'
    email_validator = EmailValidator(message=error_msg)
    email_validator(value)

    if not value.endswith("@lenta.ru"):
        raise ValidationError(error_msg)
