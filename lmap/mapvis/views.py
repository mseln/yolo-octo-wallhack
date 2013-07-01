# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context

import datetime

def hello(request):
	now = datetime.datetime.now()
	html = "<html><body>Hello world! It is now %s. </body></html>" %now
	return HttpResponse (html)

def mapapp(request):
	c = Context({'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA'})
	return render_to_response('mapvis/mapapp.html', c)
