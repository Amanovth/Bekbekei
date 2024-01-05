# Generated by Django 4.2.7 on 2024-01-05 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('home', models.CharField(max_length=100, verbose_name='Дом')),
                ('building', models.CharField(max_length=100, verbose_name='Корпус')),
                ('ward', models.CharField(max_length=100, verbose_name='Подъезд')),
                ('floot', models.CharField(max_length=100, verbose_name='Этаж')),
                ('apartment', models.CharField(max_length=100, verbose_name='Квартира')),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'Новый'), ('Cancel', 'Отмена'), ('InProgress', 'В обработке'), ('Done', 'Завершен')], default='New', max_length=100, verbose_name='Статус')),
                ('sum', models.CharField(max_length=100, verbose_name='К оплате')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('number', models.CharField(max_length=20, verbose_name='Телефон номер')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.deliveryaddress')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='TeleBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_token', models.CharField(max_length=150, verbose_name='Токен')),
                ('chat_id', models.CharField(help_text='ID группы можно узнать в веб-версии Telegram.', max_length=50, verbose_name='ID группы')),
            ],
            options={
                'verbose_name': 'Телеграм Бот',
                'verbose_name_plural': 'Настройка телеграм бота',
            },
        ),
        migrations.CreateModel(
            name='ProductInline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, verbose_name='Товар')),
                ('count', models.IntegerField(verbose_name='Кол-во')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_for_order', to='order.order')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]