from django.shortcuts import render_to_response
from django.template import Template, Context

def mapapp(request):
    now = datetime.datetime.now()
    c = Context({'NOW': now})
    return render_to_response('mapvis/mapapp.html', c)
