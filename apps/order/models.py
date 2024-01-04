from django.db import models
from apps.products.models import Product as another_model_product
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from apps.user.models import User

class TeleBot(models.Model):
    bot_token = models.CharField('Токен', max_length=150)
    chat_id = models.CharField('ID группы', max_length=50, help_text='ID группы можно узнать в веб-версии Telegram.')

    def __str__(self):
        return format_html(f'<b style="color:red;">Настроить бот!</b>')
    
    class Meta:
        verbose_name = 'Телеграм Бот'
        verbose_name_plural = 'Настройка телеграм бота'


class Order(models.Model):
    STATUS_TYPE = (
        ('New', 'Новый'),
        ('Cancel', 'Отмена'),
        ('InProgress', 'В обработке'),
        ('Done', 'Завершен')
    )
    status = models.CharField(_('Статус'), max_length=100, default='New', choices=STATUS_TYPE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(_('Имя'), max_length=100)
    last_name = models.CharField(_('Фамилия'), max_length=100)
    number = models.CharField(_('Телефон номер'), max_length=20)

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


class ProductInline(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_for_order')
    # product = models.ForeignKey(another_model_product, verbose_name=_("Товар"), on_delete=models.SET_NULL, null=True, blank=True)
    product = models.CharField(_('Товар'), max_length=500)
    count = models.IntegerField(_('Кол-во'))

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
