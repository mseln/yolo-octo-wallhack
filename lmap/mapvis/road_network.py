
from mapvis.store import *
from algorithms import *
import dijkstra
import graph

class RoadNetwork :
	def __init__(self, osm_file) :
		# Parse node and road data from osmfile
		self.nodes = StoreNodes(osm_file)
		self.roads = StoreRoads(osm_file)
		# Only chose node within a certain area
		self.nodes = ClipNodes(self.nodes.nodes, 58.3900, 58.4200, 15.5500, 15.5900)
		# nodes = ClipNodes(data.nodes, 58.3980, 58.3990, 15.5740, 15.5750)

		# Extract edges from all roads and remove all nodes that aren't connected to any road
		self.edges = self.roads.return_edges(self.nodes.return_nodes())
		self.nodes.filter(self.edges)

		# Create an adjacency list of all edges and nodes
		self.adj_list = graph.AdjList(self.nodes.return_nodes(), self.roads.return_edges(self.nodes.return_nodes()))

	def calc_shortest_path(self, post) :
		# Get closest node from POST input
		start_node = find_closest_node(graph.Node(None, post.lng1, post.lat1), self.nodes.return_nodes())
		target_node = find_closest_node(graph.Node(None, post.lng2, post.lat2), self.nodes.return_nodes())

		# Calculate the shortest path with dijkstras
		self.shortest_path = dijkstra.adjlist(self.adj_list.get_list(), start_node, target_node)

	def return_road_network(self) :
		# Get nodes in pairs between which there's an edge
		# (Only used for graphical purposes)
		return attach_edges_with_nodes(self.edges, self.nodes.return_nodes()).values()

	def return_shortest_path(self) :
		# Create a dictionary with all nodes in the shortest path
		nodes_in_shortest_path = dict() 
		if self.shortest_path : nodes_in_shortest_path = self.nodes.get_nodes(self.shortest_path['path'])
		return nodes_in_shortest_path
