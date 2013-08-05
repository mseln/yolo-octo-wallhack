import os
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context, RequestContext
from django.core import serializers
from django.core.context_processors import csrf

import datetime

from road_network import RoadNetwork
from POST_parser import POST_parser

class MapInfo :
	def __init__(self, zoom, lat, lng) :
		self.zoom = zoom
		self.lat = lat
		self.lng = lng

def hello(request):
	now = datetime.datetime.now()
	html = "<html><body>Hello world! It is now %s. </body></html>" %now
	return HttpResponse (html)

def mapapp(request):
	c = {}
	c.update(csrf(request))

	# Get values from the forms that you can see in the UI
	# If empty or not "floatable" assign them with None
	post = POST_parser(request)

	road_network = RoadNetwork(os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	road_network.calc_shortest_path(post)

	c = RequestContext(	request, 
				        {	'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA',
				         	'MAP_INFO': post,
				         	'COORDS': None , 
							# 'COORDS': nodes.nodes.values() , 
							'SHORTEST_PATH': road_network.return_shortest_path() ,
							'ROADS': road_network.return_road_network() ,
						}
					  )

	return render_to_response('mapvis/mapapp.html', c)
