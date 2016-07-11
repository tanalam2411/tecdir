from django.template import loader
from django.http import HttpResponse


def ubuntu_home(request):
    """
    :param request:
    :return: python_home python's home page: http://www.tecdir.com/ubuntu/
    """
    context = {}
    template = loader.get_template('ubuntu_app/ubuntu_home.html')
    return HttpResponse(template.render(context), request)
