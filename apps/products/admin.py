from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category, SubCategory

from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer


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


# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "cat",)
#     list_display_links = ("id", "name",)
#     list_filter = ("cat",)


@admin.register(Product)
class ProductAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ("id", "title", "code", "sub_cat", "get_html_img", "status")
    list_editable = ["status"]
    list_display_links = ("id", "title", "code",)
    search_fields = ("title", "code",)
    list_filter = ("cat", "sub_cat",)
    fields = ("sub_cat", "title", "code", "old_price", "price", "price_for", "img", "sales")
    save_as = True
    # readonly_fields = ("sales",)

    def get_html_img(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' height='60'>")

    get_html_img.short_description = "Изображение"


    @button(permission='demo.add_demomodel1',
            change_form=True,
            html_attrs={'style': 'background-color:#00ff00; color:black'})
    def refresh(self, request):
        self.message_user(request, 'Список товаров обновлен!')
        return HttpResponseRedirectToReferrer(request)