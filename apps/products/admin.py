from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category, SubCategory, UnloadedCategories, UnloadedProducts

from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from .API import update_products


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_html_img",)
    list_display_links = ("id", "name",)
    inlines = (SubCategoryInline,)

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' height='60'>")

    get_html_img.short_description = "Изображение"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "barrcode", "sub_cat", "get_html_img", "status")
    list_editable = ["status"]
    list_display_links = ("id", "title",)
    search_fields = ("title", "code", "barrcode")
    list_filter = ("cat", "sub_cat",)
    fields = ("status", "sub_cat", "title", "barrcode", "code", "old_price", "price", "wholesale_price", "price_for", "img", "sales")
    save_as = True

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' height='60'>")

    get_html_img.short_description = "Изображение"
    

admin.site.register(UnloadedCategories)


@admin.register(UnloadedProducts)
class UnloadedProductsAdmin(admin.ModelAdmin):
    list_display = ("cat", "created_at", "status")

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "cat",
                ),
            },
        ),
    )
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)