# Generated by Django 4.2.7 on 2023-11-13 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='link',
            field=models.CharField(blank=True, help_text='Если есть', max_length=500, null=True, verbose_name='Ссылка'),
        ),
    ]
