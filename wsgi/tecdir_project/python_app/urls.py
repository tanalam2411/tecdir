from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.python_home, name='python_home'),
]