#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.template import loader
from django.http import HttpResponse


def java_home(request):
    """
    :param request:
    :return: python_home python's home page: http://www.tecdir.com/python/
    """
    context = {}
    template = loader.get_template('java_app/java_home.html')
    return HttpResponse(template.render(context), request)
