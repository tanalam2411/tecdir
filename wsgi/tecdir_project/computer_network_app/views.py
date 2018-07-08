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


# def ccna_introdution(request):
#     """
#     :param request:
#     :return: python_tutorial_2x python 2X's tutorial home page:
#     """
#     context = {}
#
#     template = loader.get_template('computer_network_app/ccna/ccna_introdution_200-125.html')
#     return HttpResponse(template.render(context), request)
