# Create your views here.

import os
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context, RequestContext
from django.core import serializers
from django.core.context_processors import csrf

from store import *
from adj_matrix import AdjMatrix
from node import Node
from my_func import find_closest_node

import datetime

def hello(request):
	now = datetime.datetime.now()
	html = "<html><body>Hello world! It is now %s. </body></html>" %now
	return HttpResponse (html)

def mapapp(request):
	c = {}
	c.update(csrf(request))

	# Get values from the forms that you can see in the UI
	lat1 = request.POST.get('lat1', 'unknown')
	lng1 = request.POST.get('lng1', 'unknown')
	lat2 = request.POST.get('lat2', 'unknown')
	lng2 = request.POST.get('lng2', 'unknown')

	data = StoreNodes (os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	nodes = ClipNodes (data.nodes, 58.3984, 58.3990, 15.5733, 15.5760)
	roads = StoreRoads(os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	way_points = roads.return_waypoints(nodes.return_nodes())

	adj_matrix = AdjMatrix(nodes.return_node_refs(), nodes.return_nodes(), roads.return_edges(nodes.return_nodes()))

	start_node = None

	if lat1 != 'unknown' and lng1 != 'unknown' :
		start = Node(None, float(lng1), float(lat1))
		start_node = find_closest_node(start, nodes.return_nodes())
	print 'start: ' + str(start_node) + ' ' + str(lat1) + ' ' + str(lng1)

	target_node = None	
	if lat2 != 'unknown' and lng2 != 'unknown' :
		target = Node(None, float(lng2), float(lat2))
		target_node = find_closest_node(target, nodes.return_nodes())
	print 'target: ' + str(target_node) + ' ' + str(lat2) + ' ' + str(lng2)

	if start_node != None and target_node != None :
		print adj_matrix.get_shortest_path(start_node, target_node)


	c = RequestContext(request, 
			               {'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA',
											'COORDS': nodes.nodes.values() , 
											'ROADS': way_points}
										)

	return render_to_response('mapvis/mapapp.html', c)
