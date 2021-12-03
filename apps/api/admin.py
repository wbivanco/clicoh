from django.contrib import admin

from .models import Product, Order, OrderDetail


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']
    search_fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'datetime']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['cuantity', 'order', 'product']
    list_filter = ['order']
    search_fields = ['order']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
