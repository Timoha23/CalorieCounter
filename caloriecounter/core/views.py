from django.shortcuts import render

from http import HTTPStatus


def page_not_found(request, exception):
    return render(request, template_name='core/404.html', context={'path': request.path},
                  status=HTTPStatus.NOT_FOUND)


def csrf_failure(request, reason=''):
    return render(request, template_name='core/403csrf.html')


def internal_server_error(request, *args, **argv):
    return render(request, template_name='core/500.html',
                  status=HTTPStatus.INTERNAL_SERVER_ERROR)
