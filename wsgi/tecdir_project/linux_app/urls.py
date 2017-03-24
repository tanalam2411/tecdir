from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.linux_home, name='linux_home'),
    url(r'^tmux', views.tmux_tutorial, name='tmux_tutorial')
]
