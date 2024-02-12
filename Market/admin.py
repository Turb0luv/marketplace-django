from django.contrib import admin
from .models import Store, Product, Order, OrderItem, Currency


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'admin_id',
        'manager_count',
        'product_count'
    ]
    list_filter = ['name']
    list_display_links = ['admin_id']

    def admin_id(self, obj):
        return f'{obj.administrator.id}:{obj.administrator.username}'

    def manager_count(self, obj):
        return obj.manager.count()

    def product_count(self, obj):
        return obj.product.count()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'store',
        'price',
        'currency'
    ]
    list_filter = ['name', 'store', 'currency']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'store',
        'customer',
    ]
    list_filter = ['created_at', 'store', 'customer']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'product',
        'quantity',
    ]
    list_filter = ['order', 'product', 'quantity']


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name']