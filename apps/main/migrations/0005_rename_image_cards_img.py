# Generated by Django 4.2.7 on 2023-11-13 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cards'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='image',
            new_name='img',
        ),
    ]