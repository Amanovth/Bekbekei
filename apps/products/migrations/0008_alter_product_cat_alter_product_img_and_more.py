# Generated by Django 4.2.7 on 2023-11-12 15:44

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='product-detail/%Y_%m', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_for',
            field=models.IntegerField(choices=[(1, 'сом/кг'), (2, 'сом/шт')], max_length=50, verbose_name='тип цены'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_cat',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='cat', on_delete=django.db.models.deletion.CASCADE, to='products.subcategory', verbose_name='Подкатегория'),
        ),
    ]
