# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-01 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20161201_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods', verbose_name='Товар'),
        ),
    ]
