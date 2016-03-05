from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse


def python_home(request):
    """
    :param request:
    :return: python_home python's home page: http://www.tecdir.com/python/
    """
    context = {}
    template = loader.get_template('python_app/python_home.html')
    return HttpResponse(template.render(context), request)


# def home_view(request):
#     """
#     :param request: http request
#     :return: tecdir home page: http://www.tecdir.com
#     """
#     context = {}
#     template = loader.get_template('home/home.html')
#     return HttpResponse(template.render(context), request)
