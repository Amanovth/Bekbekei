from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(TeleBot)
class TeleBotAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    

class ProductInlineAdmin(admin.TabularInline):
    model = ProductInline
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInlineAdmin]

    list_display = ['id', 'name', 'products', 'productscount', 'status', 'number']
    list_display_links = None
    list_editable = ['status']

    def name(self, obj):
        return f'{obj.last_name} {obj.first_name}'
    

    def products(self, obj):
        a = ''
        for i in obj.product_for_order.all():
            a += f'{i.product}<br>'

        if obj.status == 'New':
            return format_html(f'<b style="color:#2a9400;">{a}</b>')
        
        elif obj.status == 'Cancel':
            return format_html(f'<b style="color:red;">{a}</b>')
        
        else:
            return format_html(a)

    products.short_description = 'Товары'


    def productscount(self, obj):
        a = ''
        for i in obj.product_for_order.all():
            a += f'{i.count}<br>'

        if obj.status == 'New':
            return format_html(f'<b style="color:#2a9400;">{a}</b>')
        
        elif obj.status == 'Cancel':
            return format_html(f'<b style="color:red;">{a}</b>')
        
        else:
            return format_html(a)

    productscount.short_description = 'Кол-во'


    def has_add_permission(self, request):
        return False


