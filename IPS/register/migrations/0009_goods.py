# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20161002_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GoodName', models.CharField(max_length=100)),
                ('AddDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
