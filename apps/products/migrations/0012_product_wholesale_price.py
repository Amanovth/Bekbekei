# Generated by Django 4.2.7 on 2024-01-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wholesale_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Оптовая цена'),
        ),
    ]