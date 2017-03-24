
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


def python_tutorial_2x(request):
    """
    :param request:
    :return: python_tutorial_2x python 2X's tutorial home page:
    """
    context = {}
    template = loader.get_template('python_app/python_tutorial_2x/python_tutorial_2x_home.html')
    return HttpResponse(template.render(context), request)


def python_tutorial_3x(request):
    """
    :param request:
    :return:
    """
    context = {}
    template = loader.get_template('python_app/python_tutorial_3x/python_tutorial_3x_home.html')
    return HttpResponse(template.render(context), request)


def flask_tutorial(request):
    """
    Args:
        request:

    Returns: flask_tutorial flask tutorial's home page.

    """
    context = {}
    template = loader.get_template('python_app/flask_tutorial/flask_tutorial_home.html')
    return HttpResponse(template.render(context), request)


