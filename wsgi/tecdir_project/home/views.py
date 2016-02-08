from django.template import loader
from django.http import HttpResponse


def home_view(request):
    """
    :param request: http request
    :return: tecdir home page: http://www.tecdir.com
    """
    context = {}
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render(context), request)

