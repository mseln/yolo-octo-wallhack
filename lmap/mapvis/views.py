# Create your views here.

import os
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context
from django.core import serializers

from store import StoreNodes, ClipNodes
from datatypes import Road, StoreRoads
from adj_matrix import AdjMatrix

import datetime

def hello(request):
	now = datetime.datetime.now()
	html = "<html><body>Hello world! It is now %s. </body></html>" %now
	return HttpResponse (html)

def mapapp(request):
	data = StoreNodes ( os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	nodes = ClipNodes ( data.nodes , 58.3984 , 58.3990 ,15.5733 , 15.5760 )
	
	roads = StoreRoads( os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	way_points = roads.return_waypoints(nodes.return_nodes())

	adj_matrix = AdjMatrix(nodes.return_node_refs(), nodes.return_nodes(), roads.return_edges(nodes.return_nodes()))
	adj_matrix.print_adjmat()

	c = Context( {'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA', 'COORDS': nodes.nodes.values() , 'ROADS': way_points})

	return render_to_response('mapvis/mapapp.html', c)
