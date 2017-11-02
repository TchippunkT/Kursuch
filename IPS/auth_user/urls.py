from django.conf.urls import url

from . import views

app_name = 'auth_users'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'auth/$', views.LoginFormView.as_view(), name='auth'),
    url(r'logout/$', views.logout_user, name="logout_user"),
]