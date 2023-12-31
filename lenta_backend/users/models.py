from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_domain


class User(AbstractUser):
    '''Модель для хранения данных о пользователе.'''

    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        'Адрес электронной почты',
        validators=(validate_domain,),
        blank=False,
        null=False,
    )
    username = models.CharField(
        'Логин',
        blank=False,
        null=False,
        max_length=32,
        unique=True,
    )
    position = models.CharField(
        'Должность',
        max_length=150,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.first_name, self.last_name}, {self.position}'
