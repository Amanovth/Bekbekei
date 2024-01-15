from django.contrib import admin
from .models import *
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
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

    list_display = ['id', 'name', 'products', 'productscount', 'status', 'number', 'address_list', 'sum']
    list_display_links = ['id', 'name', 'products', 'productscount']
    list_editable = ['status']

    def name(self, obj):
        return f'{obj.last_name} {obj.first_name}'
    
    name.short_description = format_html(f'<span style="color:#007bff;">ФИО</span>')

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

    products.short_description = format_html(f'<span style="color:#007bff;">Товары</span>')


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

    productscount.short_description = format_html('<span style="color:#007bff;">Кол-во</span>')

    def address_list(self, obj):
        if obj.address:
            return f'{obj.address.address}'

    address_list.short_description = format_html('<span style="color:#007bff;">Адрес</span>')

    def has_add_permission(self, request):
        return False


class OrderTableInfoInline(admin.TabularInline):
    model = OrderTableInfo
    extra = 0

@admin.register(OrderTable)
class OrderTableAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    inlines = [OrderTableInfoInline]
    list_display = ['id', 'get_product', 'user_info', 'phone', 'count', 'done']
    list_display_links = ['id', 'get_product', 'user_info', 'phone', 'count', 'done']

    def get_product(self, obj):
        return format_html(f'<div style="text-align: center;"><b style="font-size: 20px; color: #381a01">{obj.product}</b></div>')
    
    get_product.short_description = 'Товар'

    def user_info(self, obj):
        a = ''
        order_info = obj.order_info.all()
        for i in order_info:
            if not i.done:
                a += f'<b style="color: green;">{i.user_info}</b><br>'
            else: 
                a += f'<b style="color: red;">{i.user_info}</b><br>'
        return format_html(a)

    user_info.short_description = 'Покупатель'

    def phone(self, obj):
        a = ''
        order_info = obj.order_info.all()
        for i in order_info:
            if not i.done:
                a += f'<b style="color: green;">{i.user}</b><br>'
            else: 
                a += f'<b style="color: red;">{i.user}</b><br>'

        return format_html(a)

    phone.short_description = 'Телефон'

    def count(self, obj):
        a = ''
        order_info = obj.order_info.all()
        for i in order_info:
            if not i.done:
                a += f'<b style="color: green;">{i.count}</b><br>'
            else: 
                a += f'<b style="color: red;">{i.count}</b><br>'

        return format_html(a)

    count.short_description = 'Кол-во'

    def done(self, obj):
        a = ''
        order_info = obj.order_info.all()
        for i in order_info:
            if i.done:
                a += f'Доставлено!<br>'
            else:
                a += f'-<br>'

        return format_html(a)

    done.short_description = 'Доставлено!'


    @button(
            change_form=True,
            html_attrs={'style': 'background-color:#da2222; color:white; padding: 0.563rem 2.75rem; border-radius: 0.25rem;'})
            
    def clear(self, request):
        for i in OrderTable.objects.all():
            i.delete()
        
        self.message_user(request, 'Таблица очищена!')
        return HttpResponseRedirectToReferrer(request)
    
    clear.short_desctiprion = 'Очистить таблицу'
