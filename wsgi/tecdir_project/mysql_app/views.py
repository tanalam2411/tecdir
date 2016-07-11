from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def mysql_home(request):
    """
    :param request:
    :return: mysql_home mysql's home page: http://www.tecdir.com/myqsl/
    """
    context = {}
    template = loader.get_template('mysql_app/mysql_home.html')
    return HttpResponse(template.render(context), request)
