from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.computer_network_home, name='computer_network_home')
]
