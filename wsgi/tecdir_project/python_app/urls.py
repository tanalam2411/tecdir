from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.python_home, name='python_home'),
    url(r'^python2x/', views.python_tutorial_2x, name="python2x"),
    url(r'^python3x/', views.python_tutorial_3x, name="python3x")
]