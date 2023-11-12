# Generated by Django 4.2.7 on 2023-11-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_for',
            field=models.IntegerField(choices=[(1, 'кг'), (2, 'шт')], verbose_name='Цена за'),
        ),
    ]