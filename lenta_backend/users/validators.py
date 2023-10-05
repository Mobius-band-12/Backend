from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def validate_domain(value):
    error_msg = 'Используйте почтовый адрес на домене lenta'

    email_validator = EmailValidator(message=error_msg)
    email_validator(value)

    if not value.endswith("@lenta.ru"):
        raise ValidationError(error_msg)
