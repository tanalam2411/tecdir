from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.linux_home, name='linux_home'),
    url(r'^tmux', views.tmux_tutorial, name='tmux_tutorial'),
    url(r'^blogs/home', views.blogs_home, name='blogs_home'),
    url(r'^blogs/how-to-install-postgres-on-centos', views.install_postgres_on_centos, name='install_postgres_on_centos'),
    url(r'^blogs/how-to-install-python-on-centos', views.install_python_on_centos, name='install_python_on_centos'),
    url(r'^blogs/how-to-install-rabbitmq-on-centos', views.install_rabbitmq_on_centos, name='install_rabbitmq_on_centos')
]
