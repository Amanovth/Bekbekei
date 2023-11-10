import os
import random
import qrcode
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from .managers import CustomUserManager
from .choices import *


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    phone = models.CharField('Номер телефона', unique=True)
    
    code = models.IntegerField('Код активации', null=True, blank=True)
    activated = models.BooleanField('Активировано', default=False)
    
    bonus_id = models.CharField('Бонусный ID', null=True, blank=True)
    bonus = models.DecimalField('Бонус пользователя', max_digits=10, decimal_places=2, null=True, blank=True)
    qrimg = models.ImageField('QRcode Пользователя', null=True, blank=True)

    USERNAME_FIELD = "phone"
    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)  # Вернем номер телефона в виде строки

    def save(self, *args, **kwargs):
        bonus_id = f"312{self.phone}"
        self.bonus_id = bonus_id
        self.code = int(random.randint(100_000, 999_999))

        super(User, self).save(*args, **kwargs)

        qr = qrcode.make(str(bonus_id))
        qr_path = f'user/bonus-qr/{bonus_id}.png'
        qr.save(os.path.join(settings.MEDIA_ROOT, qr_path))
        self.qrimg.name = qr_path

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_detail")
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    birthday = models.DateField('Дата рождения')
    gender = models.CharField('Пол', max_length=50, choices=GENDERS_CHOICES)
    language = models.CharField('Родной язык', max_length=50, choices=LANGUAGE_CHOICES)
    married = models.CharField('Семейное положение', max_length=100, choices=MARRIED_CHOICES)
    status = models.CharField('Социальный статус', max_length=100, choices=SOCIAL_STATUS_CHOICES)
    city = models.CharField('Город проживания', max_length=100, choices=CITY_CHOICES)
    children = models.BooleanField('Наличие детей', default=False)
    animal = models.BooleanField('Наличие домашних животных', default=False)
    car = models.BooleanField('Наличие автомобиля', default=False)