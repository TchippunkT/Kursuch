from django.contrib import admin
from .models import Goods

# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('good_name', 'good_description', 'good_amount', 'good_price')

admin.site.register(Goods, GoodsAdmin)