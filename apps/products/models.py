from django.db import models
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField("Название", max_length=200)
    img = models.ImageField("Изображение", upload_to="product-category/%Y_%m")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="sub_categories")
    name = models.CharField("Название", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    PRICE_FOR_CHOICES = [
        (1, "кг"),
        (2, "шт")
    ]

    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    sub_cat = GroupedForeignKey(SubCategory, "cat", verbose_name="Подкатегория")
    title = models.CharField("Название товара", max_length=300)
    code = models.CharField("Код товара", max_length=100)
    pack = models.CharField('(Если упаковано - null) или "/480" г', max_length=20)
    old_price = models.CharField("Старая цена", max_length=100, blank=True, null=True)
    price = models.IntegerField("Цена")
    price_for = models.IntegerField("Цена за", choices=PRICE_FOR_CHOICES)
    img = models.ImageField("Изображение", upload_to="product-detail/%Y_%m")
    sales = models.IntegerField(_("Количество продаж"), default=0)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def save(self, *args, **kwargs):
        # Set the cat based on the selected sub_cat
        if self.sub_cat:
            self.cat = self.sub_cat.cat
        super().save(*args, **kwargs)

# class NewsPaperInfo(models.Model):
#     MONTHS = [
#         ("1", "Январь"),
#         ("2", "Февраль"),
#         ("3", "Март"),
#         ("4", "Апрель"),
#         ("5", "Май"),
#         ("6", "Июнь"),
#         ("7", "Июль"),
#         ("8", "Август"),
#         ("9", "Сентябрь"),
#         ("10", "Октябрь"),
#         ("11", "Ноябрь"),
#         ("12", "Декабрь")
#     ]
#     month = models.CharField("Текущий месяц", max_length=15, choices=MONTHS, default=None)
#     year = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name = "Газета"
#         verbose_name_plural = "Газеты"


# class NewsPaper(models.Model):
#     paper = models.ForeignKey(NewsPaperInfo, on_delete=models.CASCADE, related_name="newspaper_image")
#     images = models.ImageField("Газеты", upload_to="newpapers/%Y_%m")


# class Cards(models.Model):
#     from_date = models.DateField("Дата начала акции", blank=True, null=True)
#     from_date_after = models.CharField(blank=True, null=True, max_length=5, editable=False)
#     to_date = models.DateField("Дата окончания акции", blank=True, null=True)
#     to_date_after = models.CharField(blank=True, null=True, max_length=5, editable=False)
#     TYPES = [
#         ("1", "Успей купить"),
#         ("2", "Специальные предложения")
#     ]
#     type = models.CharField("Тип", max_length=50, choices=TYPES)
#     title = models.CharField("Название", max_length=150, help_text="Успей купить!")
#     image = models.ImageField("Картинка", upload_to="promotions/%Y_%m")

#     def save(self, *args, **kwargs):
#         self.from_date_after = self.from_date.strftime("%d.%m")
#         self.to_date_after = self.to_date.strftime("%d.%m")
#         super(Cards, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name = "Карточка"
#         verbose_name_plural = "Карточки (Акция/Предложения)"


# class Map(models.Model):
#     WORK_TIME_TYPE = [
#         ("1", "круглосуточно"),
#         ("2", "ежедневно с")
#     ]

#     name = models.CharField("Название магазина", max_length=50, help_text="Бекбекей - 1 (Бишкек)")
#     locate = models.CharField("Ориентир", max_length=150)
#     phone = models.IntegerField("Телефон номер", blank=True, null=True)
#     work_time = models.CharField("Время работы", max_length=50, choices=WORK_TIME_TYPE)
#     from_time = models.TimeField("Время ОТ", blank=True, null=True, help_text='Если время работы - "ежедневно с" то укажите время!')
#     from_time_after = models.CharField(max_length=5, blank=True, null=True, editable=False)
#     to_time = models.TimeField("Время ДО", blank=True, null=True, help_text='Если время работы - "ежедневно с" то укажите время')
#     to_time_after = models.CharField(max_length=5, blank=True, null=True, editable=False)

#     def save(self, *args, **kwargs):
#         self.from_time_after = self.from_time.strftime("%H:%M")
#         self.to_time_after = self.to_time.strftime("%H:%M")
#         super(Map, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name = "Карта"


# class DelAddress(models.Model):
#     city = models.CharField("Город", max_length=50)
#     street = models.CharField("Улица", max_length=50)
#     home = models.CharField("Дом", max_length=10)
#     frame = models.CharField("Корпус", max_length=50, blank=True, null=True)
#     entrance = models.CharField("Подъезд", max_length=50, blank=True, null=True)
#     floor = models.CharField("Этаж", max_length=50, blank=True, null=True)
#     apartment = models.CharField("Квартира", max_length=50, blank=True, null=True)
