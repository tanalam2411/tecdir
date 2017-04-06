from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def ccna_introdution(request):
    """
    :param request:
    :return: python_tutorial_2x python 2X's tutorial home page:
    """
    context = {}

    template = loader.get_template('computer_network_app/ccna/ccna_introdution.html')
    return HttpResponse(template.render(context), request)
