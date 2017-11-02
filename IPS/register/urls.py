from django.conf.urls import url

from . import views

app_name = 'register'
urlpatterns = [
    url(r'^registration/', views.RegisterFormView, name='index'),
    url(r'^users/$', views.users),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.details),
]