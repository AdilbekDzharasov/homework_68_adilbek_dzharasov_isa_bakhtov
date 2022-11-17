from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        null=False,
        blank=False,
        max_length=100
    )

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return f'{self.name}'


class Account(AbstractUser):
    OTHER = "Другое"

    GENDER_CHOICES = (
        ('O', 'Другое'),
        ('M', "Мужской"),
        ('W', "Женский"),
    )
    role = models.ForeignKey(
        to='accounts.Role',
        verbose_name='Роль',
        on_delete=models.CASCADE,
        related_name='account',
        null=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        null=False,
        blank=False
    )
    username = models.CharField(
        verbose_name='Имя',
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to='photo',
        verbose_name='Фото'
    )
    phone = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name='Номер телефона'
    )
    gender = models.CharField(
        verbose_name='Пол',
        choices=GENDER_CHOICES,
        max_length=100,
        default=OTHER
    )
    facebook = models.CharField(
        max_length=60,
        null=True,
        blank=True
    )
    telegram = models.CharField(
        max_length=60,
        null=True,
        blank=True
    )
    linkedin = models.CharField(
        max_length=60,
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'username',
        'password'
    ]

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.username} - {self.role}'

