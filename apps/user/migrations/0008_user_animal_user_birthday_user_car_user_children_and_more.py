# Generated by Django 4.2.7 on 2023-11-12 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='animal',
            field=models.BooleanField(default=False, verbose_name='Наличие домашних животных'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='car',
            field=models.BooleanField(default=False, verbose_name='Наличие автомобиля'),
        ),
        migrations.AddField(
            model_name='user',
            name='children',
            field=models.BooleanField(default=False, verbose_name='Наличие детей'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Кант', 'Кант'), ('Токмок', 'Токмок'), ('Чолпон-Ата', 'Чолпон-Ата'), ('Кара-Балта', 'Кара-Балта'), ('Сокулук', 'Сокулук'), ('Бостери', 'Бостери'), ('Балыкчы', 'Балыкчы'), ('Беловодское', 'Беловодское'), ('Ош', 'Ош'), ('Каракол', 'Каракол'), ('Базар-Коргон', 'Базар-Коргон'), ('Другой город', 'Другой город')], default='Бишкек', max_length=100, verbose_name='Город проживания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский')], default='m', max_length=50, verbose_name='Пол'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('KGZ', 'Кыргызча'), ('RU', 'Русский')], default='KGZ', max_length=50, verbose_name='Родной язык'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='married',
            field=models.CharField(choices=[('yes', 'Холост/не замужем'), ('no', 'Женат/замужем')], default='yes', max_length=100, verbose_name='Семейное положение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Домохозяйка', 'Домохозяйка'), ('Студент', 'Студент'), ('Пенсионер', 'Пенсионер'), ('Государственный служащий', 'Государственный служащий'), ('Сотрудник частной компании', 'Сотрудник частной компании'), ('Безработный', 'Безработный'), ('Частный предприниматель', 'Частный предприниматель'), ('Другое', 'Другое')], default=django.utils.timezone.now, max_length=100, verbose_name='Социальный статус'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]