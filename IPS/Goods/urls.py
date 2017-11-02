from django.conf.urls import url

from . import views

app_name = 'Goods'
urlpatterns = [
    url(r'^$', views.GoodsView, name='index'),
    url(r'^(?P<Goods_id>[0-9]+)$', views.GoodView, name='gv'),
]