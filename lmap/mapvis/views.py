import os
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Template, Context, RequestContext
from django.core import serializers
from django.core.context_processors import csrf

from store import *
from my_func import *
import dijkstra
from POST_parser import POST_parser
import graph

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

def mapapp(request):
	c = {}
	c.update(csrf(request))

	# Get values from the forms that you can see in the UI
	# If empty or not "floatable" assign them with None
	post = POST_parser(request)

	# Parse node and road data from osmfile
	nodes = StoreNodes(os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	roads = StoreRoads(os.environ['HOME'] + '/Desktop/TDDD63/lmap/mapvis/linkoping_map.osm')
	# Only chose node within a certain area
	nodes = ClipNodes(nodes.nodes, 58.3900, 58.4200, 15.5500, 15.5900)
	# nodes = ClipNodes(data.nodes, 58.3980, 58.3990, 15.5740, 15.5750)

	# Extract edges from all roads and remove all nodes that isn't connected to any road
	edges = roads.return_edges(nodes.return_nodes())
	nodes.filter(edges)

	# Create an adjacency list of all edges and nodes
	adj_list = graph.AdjList(nodes.return_nodes(), roads.return_edges(nodes.return_nodes()))

	# Get closest node from POST input
	start_node = find_closest_node(graph.Node(None, post.lng1, post.lat1), nodes.return_nodes())
	target_node = find_closest_node(graph.Node(None, post.lng2, post.lat2), nodes.return_nodes())

	# Calculate the shortest path with dijkstras
	shortest_path = dijkstra.adjlist(adj_list.get_list(), start_node, target_node)

	# Create a dictionary with all nodes in the shortest path
	nodes_in_shortest_path = dict() 
	if shortest_path : nodes_in_shortest_path = nodes.get_nodes(shortest_path['path'])
	
	# Get nodes in pairs between which there's an edge
	# (Only used for graphical purposes)
	n = attach_edges_with_nodes(edges, nodes.return_nodes())

	c = RequestContext(	request, 
				        {	'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA',
				         	'MAP_INFO': post,
				         	'COORDS': None , 
							# 'COORDS': nodes.nodes.values() , 
							'ROAD': nodes_in_shortest_path ,
							'ROADS': n.values()
						}
					  )

	return render_to_response('mapvis/mapapp.html', c)
