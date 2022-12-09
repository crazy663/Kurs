from django.http import HttpResponse
import Pars

def index(request,html ):
    return HttpResponse(f"Полученный HTML: {Pars.get_content(html)}")