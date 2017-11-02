#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class AuthForm(AuthenticationForm):

    username = forms.CharField(label = "",widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class':'authform'}))
    password = forms.CharField(label = "",widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'type':'password','class':'authform'}))
