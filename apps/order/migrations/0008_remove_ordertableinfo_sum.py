# Generated by Django 4.2.7 on 2024-01-16 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_ordertable_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertableinfo',
            name='sum',
        ),
    ]
