from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.mysql_home, name='mysql_home')
]
