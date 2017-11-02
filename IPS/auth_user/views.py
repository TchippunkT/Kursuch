#!/usr/bin/python3
# -*- coding:utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import AuthForm




class LoginFormView(FormView):
    form_class = AuthForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def index(request):
    return HttpResponseRedirect("/goods/")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")