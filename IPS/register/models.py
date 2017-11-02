# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение')
    cartids = models.CharField(max_length=9, blank=True)

    def __str__(self):
        return self.user.first_name
# class Goods(models.Model):
#     GoodName = models.CharField(max_length=100)
#     AddDate = models.DateTimeField(auto_now_add=True)