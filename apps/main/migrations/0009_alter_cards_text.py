# Generated by Django 4.2.7 on 2023-11-20 08:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_cards_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
