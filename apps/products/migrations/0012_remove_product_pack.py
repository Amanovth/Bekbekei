# Generated by Django 4.2.7 on 2023-11-15 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_price_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pack',
        ),
    ]
