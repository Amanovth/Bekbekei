# Generated by Django 4.2.7 on 2023-11-13 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_image_cards_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='from_date',
            new_name='datefrom',
        ),
        migrations.RenameField(
            model_name='cards',
            old_name='to_date',
            new_name='dateto',
        ),
        migrations.RemoveField(
            model_name='cards',
            name='from_date_after',
        ),
        migrations.RemoveField(
            model_name='cards',
            name='to_date_after',
        ),
    ]
