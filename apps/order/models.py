from django.db import models
from apps.products.models import Product as another_model_product
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from apps.user.models import User
from django.db.models import F, Sum


class TeleBot(models.Model):
    bot_token = models.CharField('Токен', max_length=150)
    chat_id = models.CharField('ID группы', max_length=50, help_text='ID группы можно узнать в веб-версии Telegram.')

    def __str__(self):
        return format_html(f'<b style="color:red;">Настроить бот!</b>')
    
    class Meta:
        verbose_name = 'Телеграм Бот'
        verbose_name_plural = 'Настройка телеграм бота'


class OrderTable(models.Model):
    product = models.CharField('Товар', blank=True, null=True)
    count = models.IntegerField('Общее количество', blank=True, null=True)
    
    class Meta:
        verbose_name = "Таблица заказов"
        verbose_name_plural = "Таблица заказов"

    # def save(self, *args, **kwargs):
    #     order = self.order_info.all()
    #     sum = 0
    #     for i in order:
    #         sum += i(i.sum)
    #     super(OrderTable, self).save(*args, **kwargs)

    # def __str__(self):
    #     return f'{self.product}'

class OrderTableInfo(models.Model):
    order = models.ForeignKey(OrderTable, on_delete=models.CASCADE, related_name='order_info')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Покупатель")
    user_info = models.CharField('ФИО', max_length=200, blank=True, null=True, default=120)
    count = models.IntegerField('Кол-во')
    done = models.BooleanField(default=False, verbose_name='Доставлено!')

    def save(self, *args, **kwargs):
        self.user_info = f'{self.user.first_name} {self.user.last_name}'
        super(OrderTableInfo, self).save(*args, **kwargs)


class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    address = models.CharField(_('Город'), max_length=100)

    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.address}'

class Order(models.Model):
    STATUS_TYPE = (
        ('New', 'Новый'),
        ('Cancel', 'Отмена'),
        ('InProgress', 'В обработке'),
        ('Done', 'Завершен')
    )
    status = models.CharField(_('Статус'), max_length=100, default='New', choices=STATUS_TYPE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    sum = models.CharField(_('К оплате'), max_length=100)
    address = models.ForeignKey(DeliveryAddress, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(_('Имя'), max_length=100)
    last_name = models.CharField(_('Фамилия'), max_length=100)
    number = models.CharField(_('Телефон номер'), max_length=20)
    datetime = models.CharField(_("Дата и время заказа"), max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

        related_products = self.product_for_order.all()

        for i in related_products:
            order_table, created = OrderTable.objects.get_or_create(product=i.product)

            if created:
                order_info = OrderTableInfo.objects.create(order=order_table, user=self.user, count=i.count)
            else:
                order_info_exists = OrderTableInfo.objects.filter(order=order_table, user=self.user).exists()
                order_info_done = OrderTableInfo.objects.filter(order=order_table, user=self.user, done=False).exists()

                if order_info_exists and order_info_done:
                    order_info = OrderTableInfo.objects.get(order=order_table, user=self.user, done=False)
                    order_info.count = F('count') + i.count
                    order_info.save()
                else:
                    order_info = OrderTableInfo.objects.create(order=order_table, user=self.user, count=i.count)

        order_tables = OrderTable.objects.annotate(total_count=Sum('order_info__count'))
        for order_table in order_tables:
            order_table.count = order_table.total_count
            order_table.save()
    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


class ProductInline(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_for_order')

    # product = models.ForeignKey(another_model_product, verbose_name=_("Товар"), on_delete=models.SET_NULL, null=True, blank=True)
    product = models.CharField(_("Товар"), max_length=100)
    count = models.IntegerField(_('Кол-во'))
    price_for = models.CharField("Цена за", blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


