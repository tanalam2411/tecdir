from django.conf.urls import url
from . import views
from . import ccna_views

urlpatterns = [
    url(r'^$', views.computer_network_home, name='computer_network_home'),
    url(r'^ccna/introduction', ccna_views.ccna_introdution, name="ccna/introduction"),
]
