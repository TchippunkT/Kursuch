# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-01 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0001_initial'),
        ('cart', '0003_auto_20161201_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_good',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_goods',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods', verbose_name='Товар'),
        ),
    ]