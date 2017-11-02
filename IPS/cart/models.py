from django.db import models
from Goods.models import Goods
from register.models import MyUser
# Create your models here.

class Cart(models.Model):
    cart_goods = models.ForeignKey(Goods, verbose_name='Товар')
    cart_amount = models.IntegerField(verbose_name='Количество')
    cart_user = models.ForeignKey(MyUser, verbose_name='Пользователь')
    cart_sum = models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Сумма')
    cart_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    def __str__(self):
        return self.cart_goods.good_name