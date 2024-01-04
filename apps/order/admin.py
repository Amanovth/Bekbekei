from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ProductInlineAdmin(admin.TabularInline):
    model = ProductInline
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInlineAdmin]

    list_display = ['id', 'products', 'productscount', 'status']
    list_display_links = ['id', 'products']
    list_editable = ['status']

    def products(self, obj):
        a = ''
        for i in obj.product.all():
            a += f'{i.product}<br>'
        return format_html(f'<p style="padding:0px;">{a}</p>')

    products.short_description = 'Товары'

    def productscount(self, obj):
        a = ''
        for i in obj.product.all():
            a += f'{i.count}<br>'
        return format_html(a)

    productscount.short_description = 'Кол-во'
