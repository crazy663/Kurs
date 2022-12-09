from django.http import HttpResponse

from func_app.func import  get_html


def index(request,url, params ):
    return HttpResponse(f"Полученный HTML: {get_html(url, params)}")