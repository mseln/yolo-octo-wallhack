import os
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context, RequestContext
from django.core import serializers
from django.core.context_processors import csrf

from store import *
from my_func import *
import dijkstra
import html_parser
import graph

import datetime

def hello(request):
	now = datetime.datetime.now()
	html = "<html><body>Hello world! It is now %s. </body></html>" %now
	return HttpResponse (html)

def mapapp(request):
	c = {}
	c.update(csrf(request))

	# Get values from the forms that you can see in the UI
	# If empty or not "floatable" assign them with None	
	lat1 = html_parser.get_float(request, 'lat1')
	lng1 = html_parser.get_float(request, 'lng1')
	lat2 = html_parser.get_float(request, 'lat2')
	lng2 = html_parser.get_float(request, 'lng2')
	
	data = StoreNodes (os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	nodes = ClipNodes ( data.nodes, 58.3960, 58.4040, 15.5700, 15.5790 )

	roads = StoreRoads(os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')

	adj_list = graph.AdjList(nodes.return_node_refs(), nodes.return_nodes(), roads.return_edges(nodes.return_nodes()))
	
	edges = roads.return_edges(nodes.return_nodes())
	n = attach_edges_with_nodes(edges, nodes.return_nodes())

	start_node = find_closest_node(graph.Node(None, lng1, lat1), nodes.return_nodes())
	target_node = find_closest_node(graph.Node(None, lng2, lat2), nodes.return_nodes())
	print start_node
	print target_node

	shortest_path = dijkstra.adjlist(adj_list.get_list(), start_node, target_node)

	nodes_in_shortest_path = dict() 
	if shortest_path : nodes_in_shortest_path = nodes.get_nodes(shortest_path['path'])
	
	c = RequestContext(request, 
				             {'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA',
											'COORDS': nodes.nodes.values() , 
											'ROAD': nodes_in_shortest_path ,
											'ROADS': n.values()
											}
										 )

	return render_to_response('mapvis/mapapp.html', c)
