from django.http import HttpResponse

from func_app.func import get_content


def index(request,html ):
    return HttpResponse(f"Полученный HTML: {get_content(html)}")