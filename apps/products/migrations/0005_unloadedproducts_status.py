# Generated by Django 4.2.7 on 2023-12-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_unloadedproducts_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='unloadedproducts',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Показать в мобильном приложении'),
        ),
    ]
