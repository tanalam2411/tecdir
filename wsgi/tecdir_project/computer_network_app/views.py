from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def computer_network_home(request):
    """
    :param request:
    :return: computer_network_home computer network's home page: http://www.tecdir.com/computer_network/
    """
    context = {}
    template = loader.get_template('computer_network_app/computer_network_home.html')
    return HttpResponse(template.render(context), request)

