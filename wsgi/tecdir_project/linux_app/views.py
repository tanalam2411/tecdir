
from django.template import loader
from django.http import HttpResponse



print("22222222222222222222222222222")
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


def blogs_home(request):
    """
    :param request:
    :return: tmux_tutorial tmux tutorial home page: http://www.tecdir.com/linux/tmux
    """
    context = {}
    template = loader.get_template('linux_app/linux_blogs/linux_blogs_home.html')
    return HttpResponse(template.render(context), request)

# -----------------------------------------------------------------------------

def install_postgres_on_centos(request):
    """
    :param request:
    :return: tmux_tutorial tmux tutorial home page: http://www.tecdir.com/linux/tmux
    """
    context = {}
    template = loader.get_template('linux_app/linux_blogs/install_postgres_rpm_on_centos.html')
    return HttpResponse(template.render(context), request)


def install_python_on_centos(request):
    """
    :param request:
    :return: tmux_tutorial tmux tutorial home page: http://www.tecdir.com/linux/tmux
    """
    context = {}
    template = loader.get_template('linux_app/linux_blogs/install_python_on_centos.html')
    return HttpResponse(template.render(context), request)


def install_rabbitmq_on_centos(request):
    """
    :param request:
    :return: tmux_tutorial tmux tutorial home page: http://www.tecdir.com/linux/tmux
    """
    context = {}
    template = loader.get_template('linux_app/linux_blogs/install_rabbitmq_rpm_on_centos.html')
    return HttpResponse(template.render(context), request)


# -----------------------------------------------------------------------------


def pip_install_psycopg2_on_centos(request):
    """
    :param request:
    :return: tmux_tutorial tmux tutorial home page: http://www.tecdir.com/linux/tmux
    """
    context = {}

    template = loader.get_template('linux_app/linux_prob_sols/pip_install_psycopg2_on_centos.html')
    return HttpResponse(template.render(context), request)

