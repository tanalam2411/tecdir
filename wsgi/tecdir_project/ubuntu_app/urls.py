from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ubuntu_home, name='ubuntu_home')
]