# Generated by Django 4.2.7 on 2023-11-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_cards_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='date',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Действует до:'),
        ),
    ]
