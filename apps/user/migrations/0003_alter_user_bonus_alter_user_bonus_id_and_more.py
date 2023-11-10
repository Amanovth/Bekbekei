# Generated by Django 4.2.7 on 2023-11-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bonus',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Бонус пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bonus_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Бонусный ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='qrimg',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='', verbose_name='QRcode Пользователя'),
        ),
    ]
