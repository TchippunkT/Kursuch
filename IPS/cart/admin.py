from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_goods', 'cart_amount', 'cart_user', 'cart_sum')

admin.site.register(Cart, CartAdmin)
# Register your models here.
