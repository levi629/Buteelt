from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart_id', 'created_date')
    readonly_fields = ('created_date',)
    search_fields = ('cart_id',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'quantity', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('product__product_name',)
