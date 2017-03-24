
from django.template import loader
from django.http import HttpResponse


def linux_home(request):
    """
    :param request:
    :return: linux_home linux's home page: http://www.tecdir.com/linux/
    """
    context = {}
    template = loader.get_template('linux_app/linux_home.html')
    return HttpResponse(template.render(context), request)


def tmux_tutorial(request):
    """
    :param request:
    :return: tmux_tutorial tmux tutorial home page: http://www.tecdir.com/linux/tmux
    """
    context = {}
    template = loader.get_template('linux_app/tmux_tutorial/tmux_tutorial_home.html')
    return HttpResponse(template.render(context), request)