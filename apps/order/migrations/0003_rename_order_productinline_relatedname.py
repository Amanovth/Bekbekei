# Generated by Django 4.2.7 on 2024-01-04 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_relatedname_productinline_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinline',
            old_name='order',
            new_name='relatedname',
        ),
    ]
