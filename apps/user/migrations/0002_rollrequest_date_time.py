# Generated by Django 4.2.7 on 2024-01-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rollrequest',
            name='date_time',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дата и Время'),
        ),
    ]