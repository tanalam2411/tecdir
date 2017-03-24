from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.java_home, name='java_home'),
]