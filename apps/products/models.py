import os
import requests
from django.conf import settings
from django.db import models
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from django.utils.translation import gettext_lazy as _
from PIL import Image, ImageDraw, ImageFont
from django.dispatch import receiver
from django.db.models.signals import post_save
# from .views import unload_products


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
        ("кг", "кг"),
        ("шт", "шт")
    ]

    status  = models.BooleanField(_('Показать в мобильном приложении'), default=False)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    sub_cat = GroupedForeignKey(SubCategory, "cat", verbose_name="Подкатегория", null=True, blank=True)
    title = models.CharField("Название товара", max_length=300)
    code = models.CharField("Код товара", max_length=100, null=True, blank=True, unique=True)
    # pack = models.CharField('(Если упаковано - null) или "/480" г', max_length=20)
    old_price = models.CharField("Старая цена", max_length=100, blank=True, null=True)
    price = models.FloatField("Цена")
    price_for = models.CharField("Цена за", choices=PRICE_FOR_CHOICES, default="шт")
    img = models.ImageField("Изображение", upload_to="product-detail/%Y_%m", null=True, blank=True)
    sales = models.IntegerField(_("Количество продаж"), default=0)
    quantity = models.CharField(null=True, blank=True)

    # created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", blank=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения", blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def save(self, *args, **kwargs):
        if self.sub_cat:
            self.cat = self.sub_cat.cat
        self.price = float(self.price)
        super().save(*args, **kwargs)

        if self.img:
            watermark_path = os.path.join(os.path.dirname(__file__), 'mark.png')
            watermark = Image.open(watermark_path).convert("RGBA")

            img_path = os.path.join(settings.MEDIA_ROOT, f"{self.img.name}")
            img = Image.open(img_path).convert("RGBA").copy()

            img_width, img_height = img.size
            watermark_width, watermark_height = watermark.size

            scale = 0.5
            new_watermark_width = int(img_width * scale)
            new_watermark_height = int((new_watermark_width / watermark_width) * watermark_height)
            resized_watermark = watermark.resize((new_watermark_width, new_watermark_height))

            x = (img_width - new_watermark_width) // 2
            y = (img_height - new_watermark_height) // 2

            img.paste(resized_watermark, (x, y), resized_watermark)

            img.save(img_path, format="png", quality=100)


class UnloadedCategories(models.Model):
    name = models.CharField(_("Название"), max_length=255)
    guid = models.CharField(_("GUID"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Выгруженная категория")
        verbose_name_plural = _("Выгруженные категории")


class UnloadedProducts(models.Model):
    cat = models.ForeignKey(UnloadedCategories, on_delete=models.CASCADE)
    created
    # name = models.CharField(_("Заголовок"), max_length=255, null=True, blank=True)
    # product_id = models.CharField(_("ID продукта"), max_length=255, null=True, blank=True)
    # barrcode = models.IntegerField(_("Штрих-код"), null=True, blank=True)
    # price = models.CharField(_("Цена"), max_length=20, null=True, blank=True)
    # discounted_price = models.CharField(_("Цена со скидкой"), max_length=20, null=True, blank=True)
    # quantity = models.CharField(_("Количество"), max_length=30, null=True, blank=True)
    # unit = models.CharField(_("Единица"), max_length=10, null=True, blank=True)
    # status  = models.BooleanField(_('Показать в мобильном приложении'), default=False)

    def __str__(self):
        if self.name:
            return self.name
        return self.cat. name

    class Meta:
        verbose_name = _("Выгруженный продукт")
        verbose_name_plural = _("Выгруженные продукты")

    def save(self, *args, **kwargs):
        # url = f"http://31.186.48.247/Roznica/hs/MobileApp/product-list?Guid={self.cat.guid}"
        # headers = {"Authorization": settings.ONE_C}

        # response = requests.get(url=url, headers=headers)

        # product_list = response.json()
        import json
        with open("/home/chyngyz/Bekbekei/file.json", 'r') as file:
            product_list = json.load(file)

        for product in product_list:
            obj = Product(
                # cat=self.cat,
                title=product["name"],
                code=product["product_id"],
                # barrcode=product["Barcode"],
                price=product["price"],
                old_price=product["discounted_price"],
                quantity=product["quantity"],
                price_for=product["unit"]
            )
            obj.save()

        return super(UnloadedProducts, self).save(*args, **kwargs)
