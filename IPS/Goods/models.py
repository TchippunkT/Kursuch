from django.db import models

# Create your models here.
CATEGORIES = (
    (u'Напитки','Напитки'),
    (u'Скоропортящиеся','Скоропортящиеся'),
    (u'Долгопортящиеся','Долгопортящиеся'),
)


class Goods(models.Model):
    good_name = models.CharField(max_length=200, verbose_name='Наименование')
    good_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')
    good_description = models.TextField(verbose_name='Описание')
    good_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    good_img = models.ImageField(upload_to='images/goods', verbose_name='Изображение')
    good_amount = models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Количество')
    good_category = models.CharField(choices=CATEGORIES, verbose_name='Категория', max_length=100)

    def __str__(self):
        return self.good_name