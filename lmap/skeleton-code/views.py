import os
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context, RequestContext
from django.core import serializers
from django.core.context_processors import csrf

import datetime

class MapInfo :
	def __init__(self, zoom, lat, lng) :
		self.zoom = zoom
		self.lat = lat
		self.lng = lng

def hello(request):
	now = datetime.datetime.now()
	html = "<html><body>Hello world! It is now %s. </body></html>" %now
	return HttpResponse (html)