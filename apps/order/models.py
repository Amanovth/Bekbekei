from django.db import models
from apps.products.models import Product
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    STATUS_TYPE = (
        ('New', 'Новый'),
        ('Cancel', 'Отмена'),
        ('InProgress', 'В обработке'),
        ('Done', 'Завершен')
    )
    status = models.CharField(_('Статус'), max_length=100, default='Новый', choices=STATUS_TYPE)

    # ФИО итд

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


class ProductInline(models.Model):
    relatedname = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='product')
    product = models.ForeignKey(Product, verbose_name=_("Товар"), on_delete=models.SET_NULL, null=True, blank=True)
    count = models.IntegerField(_('Кол-во'))

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
