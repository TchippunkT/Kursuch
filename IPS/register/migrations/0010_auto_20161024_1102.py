# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='AddDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]