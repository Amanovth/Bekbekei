# Generated by Django 4.2.7 on 2023-12-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_unloadedcategories_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unloadedproducts',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
