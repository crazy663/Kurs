from django.http import HttpResponse

from djangoProject import func_app
from func_app.func import get_content
from func_app import func


def index(request, urlpath=None):
    return HttpResponse(f'<h1> Подписки канала: {func.get_content(urlpath)}</h1>')
