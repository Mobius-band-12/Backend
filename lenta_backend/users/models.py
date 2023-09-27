from django.contrib.auth import models


class User(models.AbstractUser):
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
        blank=False,
        null=False,
    )
    username = models.CharField(
        'Логин',
        blank=False,
        null=False,
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
