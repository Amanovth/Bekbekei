import os
import random
import qrcode
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from .managers import CustomUserManager
from .choices import *


class User(AbstractUser):
    username = None
    phone = models.CharField("Номер телефона", unique=True)

    code = models.IntegerField("Код активации", null=True, blank=True)
    activated = models.BooleanField("Активировано", default=False)

    bonus_id = models.CharField("Бонусный ID", null=True, blank=True)
    bonus = models.DecimalField("Бонус пользователя", max_digits=10, decimal_places=2, null=True, blank=True)
    qrimg = models.ImageField("QRcode Пользователя", null=True, blank=True)

    # Detail
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=50, choices=GENDERS_CHOICES, null=True, blank=True)
    language = models.CharField("Родной язык", max_length=50, choices=LANGUAGE_CHOICES, null=True, blank=True)
    married = models.CharField("Семейное положение", max_length=100, choices=MARRIED_CHOICES, null=True, blank=True)
    status = models.CharField("Социальный статус", max_length=100, choices=SOCIAL_STATUS_CHOICES, null=True, blank=True)
    city = models.CharField("Город проживания", max_length=100, choices=CITY_CHOICES, null=True, blank=True)
    children = models.BooleanField("Наличие детей", default=False)
    animal = models.BooleanField("Наличие домашних животных", default=False)
    car = models.BooleanField("Наличие автомобиля", default=False)

    USERNAME_FIELD = "phone"
    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)  # Вернем номер телефона в виде строки

    def save(self, *args, **kwargs):
        bonus_id = f"312{self.phone}"
        self.bonus_id = bonus_id
        self.code = int(random.randint(100_000, 999_999))
        
        qr = qrcode.make(str(bonus_id), border=2)
        qr_path = f"user/bonus-qr/{bonus_id}.png"
        qr.save(os.path.join(settings.MEDIA_ROOT, qr_path))
        self.qrimg.name = qr_path

        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
