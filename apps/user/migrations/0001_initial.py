# Generated by Django 4.2.7 on 2024-01-06 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(unique=True, verbose_name='Номер телефона')),
                ('code', models.IntegerField(blank=True, null=True, verbose_name='Код активации')),
                ('activated', models.BooleanField(default=False, verbose_name='Активировано')),
                ('bonus_id', models.CharField(blank=True, null=True, verbose_name='Бонусный ID')),
                ('bonus', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Бонус пользователя')),
                ('qrimg', models.ImageField(blank=True, null=True, upload_to='', verbose_name='QRcode Пользователя')),
                ('notification', models.BooleanField(default=False, verbose_name='Получать уведомления')),
                ('auto_brightness', models.BooleanField(default=False, verbose_name='Авто яркость')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('user_roll', models.CharField(choices=[('1', 'Клиент'), ('2', 'Оптовик')], default='1', max_length=100, verbose_name='Роль')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('gender', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=50, null=True, verbose_name='Пол')),
                ('language', models.CharField(blank=True, choices=[('Кыргызча', 'Кыргызча'), ('Русский', 'Русский')], max_length=50, null=True, verbose_name='Родной язык')),
                ('married', models.CharField(blank=True, choices=[('Холост/не замужем', 'Холост/не замужем'), ('Женат/замужем', 'Женат/замужем')], max_length=100, null=True, verbose_name='Семейное положение')),
                ('status', models.CharField(blank=True, choices=[('Домохозяйка', 'Домохозяйка'), ('Студент', 'Студент'), ('Пенсионер', 'Пенсионер'), ('Государственный служащий', 'Государственный служащий'), ('Сотрудник частной компании', 'Сотрудник частной компании'), ('Безработный', 'Безработный'), ('Частный предприниматель', 'Частный предприниматель'), ('Другое', 'Другое')], max_length=100, null=True, verbose_name='Социальный статус')),
                ('city', models.CharField(blank=True, choices=[('Бишкек', 'Бишкек'), ('Кант', 'Кант'), ('Токмок', 'Токмок'), ('Чолпон-Ата', 'Чолпон-Ата'), ('Кара-Балта', 'Кара-Балта'), ('Сокулук', 'Сокулук'), ('Бостери', 'Бостери'), ('Балыкчы', 'Балыкчы'), ('Беловодское', 'Беловодское'), ('Ош', 'Ош'), ('Каракол', 'Каракол'), ('Базар-Коргон', 'Базар-Коргон'), ('Другой город', 'Другой город')], max_length=100, null=True, verbose_name='Город проживания')),
                ('children', models.BooleanField(default=False, verbose_name='Наличие детей')),
                ('animal', models.BooleanField(default=False, verbose_name='Наличие домашних животных')),
                ('car', models.BooleanField(default=False, verbose_name='Наличие автомобиля')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='RollRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(choices=[('1', 'Клиент'), ('2', 'Оптовик')], default='1', max_length=100, verbose_name='Роль')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Запрос на "Оптовик"',
                'verbose_name_plural': 'Запросы на "Оптовик"',
            },
        ),
    ]
