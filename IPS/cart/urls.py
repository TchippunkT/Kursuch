from django.conf.urls import url
from . import views

app_name = 'cart'
urlpatterns = [
    url(r'^cart/', views.CartView, name='index'),
    url(r'^buy/(?P<cart_id>[0-9]+)/$', views.CartAdd, name='adding'),
    url(r'^buy/', views.ClearCart, name='index1'),
    url(r'^order/', views.get_order, name='index2'),
]