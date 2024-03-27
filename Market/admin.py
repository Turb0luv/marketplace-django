from django.contrib import admin
from .models import Store, Product, Order, OrderItem, Currency, UserIPAddress, UserProfile


class ProductInline(admin.TabularInline):
    model = OrderItem
    extra = 1


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
    list_display_links = ['name', 'admin_id']

    def admin_id(self, obj):
        return f'{obj.administrator.id}:{obj.administrator.username}'

    def manager_count(self, obj):
        return obj.managers.count()

    def product_count(self, obj):
        return obj.product_set.count()

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('administrator')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'store_id',
        'price',
        'currency'
    ]
    list_filter = ['name', 'store', 'currency']
    list_display_links = ['name', 'store_id']

    def store_id(self, obj):
        return f'{obj.store.id}:{obj.store.name}'

    def get_queryset(self, request):

        return super().get_queryset(request).prefetch_related('store')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'store',
        'customer',
    ]
    list_filter = ['created_at', 'store', 'customer']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('store', 'customer')

    inlines = [ProductInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'product',
        'quantity',
    ]
    list_filter = ['order', 'product', 'quantity']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('order', 'product')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(UserIPAddress)
class UserIPAddressAdmin(admin.ModelAdmin):
    list_display = [
        'ip_address',
        'user',
        'last_login_time',
    ]
    list_filter = ['user', 'last_login_time']


@admin.register(UserProfile)
class UserIPAddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'last_action_time',
    ]
    list_filter = ['user', 'last_action_time']