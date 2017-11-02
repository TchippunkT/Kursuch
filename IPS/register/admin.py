# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
admin.site.unregister(User)
from .models import User,MyUser
#
# class UserInline(admin.StackedInline):
#     model = MyUser
#     can_delete = False
#     verbose_name_plural = 'Additional info'
#
# class UserAdmin(UserAdmin):
#     inlines = (UserInline,)


admin.site.register(User, UserAdmin)
admin.site.register(MyUser)
