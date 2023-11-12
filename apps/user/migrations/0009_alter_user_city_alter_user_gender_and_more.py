# Generated by Django 4.2.7 on 2023-11-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_animal_user_birthday_user_car_user_children_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, choices=[('Бишкек', 'Бишкек'), ('Кант', 'Кант'), ('Токмок', 'Токмок'), ('Чолпон-Ата', 'Чолпон-Ата'), ('Кара-Балта', 'Кара-Балта'), ('Сокулук', 'Сокулук'), ('Бостери', 'Бостери'), ('Балыкчы', 'Балыкчы'), ('Беловодское', 'Беловодское'), ('Ош', 'Ош'), ('Каракол', 'Каракол'), ('Базар-Коргон', 'Базар-Коргон'), ('Другой город', 'Другой город')], max_length=100, null=True, verbose_name='Город проживания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Мужской'), ('f', 'Женский')], max_length=50, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('KGZ', 'Кыргызча'), ('RU', 'Русский')], max_length=50, null=True, verbose_name='Родной язык'),
        ),
        migrations.AlterField(
            model_name='user',
            name='married',
            field=models.CharField(blank=True, choices=[('yes', 'Холост/не замужем'), ('no', 'Женат/замужем')], max_length=100, null=True, verbose_name='Семейное положение'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('Домохозяйка', 'Домохозяйка'), ('Студент', 'Студент'), ('Пенсионер', 'Пенсионер'), ('Государственный служащий', 'Государственный служащий'), ('Сотрудник частной компании', 'Сотрудник частной компании'), ('Безработный', 'Безработный'), ('Частный предприниматель', 'Частный предприниматель'), ('Другое', 'Другое')], max_length=100, null=True, verbose_name='Социальный статус'),
        ),
    ]