# Generated by Django 4.2.7 on 2024-01-07 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='building',
        ),
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='floot',
        ),
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='home',
        ),
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='street',
        ),
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='ward',
        ),
    ]
