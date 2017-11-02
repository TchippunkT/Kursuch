#!/usr/bin/python3
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import MyUser



class RegisterForm(UserCreationForm):
    # declare the fields you will show
    username = forms.CharField(label = "",widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(label = "",widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(label = "",widget=forms.TextInput(attrs={'placeholder': 'Никнейм'}))
    password1 = forms.CharField(label = "",widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'type':'password'}))
    password2 = forms.CharField(label = "",widget=forms.TextInput(attrs={'placeholder': 'Повторите пароль', 'type':'password'}))
    # this sets the order of the fields
    class Meta:
        model = User
        fields = ( "first_name", "username", "email","password1","password2", )


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар')
    class Meta:
        model = MyUser
        fields = ('avatar',)