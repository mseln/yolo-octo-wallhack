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
from my_func import *
from dijkstra import dijkstra

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
	nodes = ClipNodes ( data.nodes, 58.3984, 58.4002, 15.5733, 15.5760 )

	roads = StoreRoads(os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	way_points = roads.return_waypoints(nodes.return_nodes())

	
	adj_matrix = AdjMatrix(nodes.return_node_refs(), nodes.return_nodes(), roads.return_edges(nodes.return_nodes()))
	
	edges = roads.return_edges(nodes.return_nodes())
	n = attach_edges_with_nodes(edges, nodes.return_nodes())

	start_node = find_closest_node(Node(None, lng1, lat1), nodes.return_nodes())
	target_node = find_closest_node(Node(None, lng2, lat2), nodes.return_nodes())

	shortest_path = None
	nodes_in_shortest_path = dict()
	if start_node and target_node :
		shortest_path = dijkstra(adj_matrix.get_matrix(), start_node, target_node)

	print shortest_path

	it = 0
	if shortest_path != None :
		for node in shortest_path :
			nodes_in_shortest_path[it] = nodes.nodes[node]
			it += 1
	
	if (len(nodes_in_shortest_path.keys()) != 0) :
		c = RequestContext(request, 
				               {'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA',
												'COORDS': nodes.nodes.values() , 
												'ROAD': nodes_in_shortest_path}
											 )
	else :	
		c = RequestContext(request, 
				               {'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA',
												'COORDS': nodes.nodes.values(), 
												'ROADS': n.values()}
											 )

	return render_to_response('mapvis/mapapp.html', c)
