from imposm.parser import OSMParser
from node import Node, Edge
from my_func import length_haversine

# This class reads an OSM file and stores its nodes in memory
class StoreNodes(object) :
	def __init__(self, osmfile) :
		# parse the input file and save its contents in memory
		# node ids and coord pairs as returned from imposm
		self.nodes = dict()
		# actual min and max latitude and longitude of coordinates
		self.bounds = dict()
		self.bounds["min_lat"] = 9999
		self.bounds["max_lat"] = -9999
		self.bounds["min_lng"] = 9999
		self.bounds["max_lng"] = -9999
		p = OSMParser(coords_callback = self.coords_callback)
		p.parse(osmfile)
	
	def coords_callback(self, coords) :
		for osmid, lng, lat in coords :
			node = Node(osmid ,lng ,lat)
			self.nodes[osmid] = node
			self.bounds["min_lat"] = min( self.bounds["min_lat"], lat)
			self.bounds["min_lng"] = min( self.bounds["min_lng"], lng)
			self.bounds["max_lat"] = max( self.bounds["max_lat"], lat)
			self.bounds["max_lng"] = max( self.bounds["max_lng"], lng)

	def coords_print(self) :
		for node in self.nodes :
			print str(self.nodes[node].id) + '\t' + str(self.nodes[node].lng) + '\t' + str(self.nodes[node].lat)

	
	def return_nodes(self) :
		return self.nodes


# A class for storing nodes within a rectangular area
class ClipNodes :
	def __init__ ( self , nodes , minlat , maxlat , minlng , maxlng ):
		# node ids and coord pairs
		self.nodes = dict ()
		# min and max latitude and longitude
		self.minlat = minlat
		self.maxlat = maxlat
		self.minlng = minlng
		self.maxlng = maxlng

		# actual min and max latitude and longitude of coordinates
		self.bounds = dict ()
		self.bounds["min_lat"] = 9999
		self.bounds["max_lat"] = -9999
		self.bounds["min_lng"] = 9999
		self.bounds["max_lng"] = -9999
		for node in nodes.values() :
			if self.minlng < node.lng and node.lng < self.maxlng and self.minlat < node.lat and node.lat < self.maxlat :
				new_node = Node(node.id, node.lng, node.lat)
				self.nodes[node.id] = node

				# update bounds
				self.bounds["min_lat"] = min(self.bounds["min_lat"], node.lat)
				self.bounds["min_lng"] = min(self.bounds["min_lng"], node.lng)
				self.bounds["max_lat"] = max(self.bounds["max_lat"], node.lat)
				self.bounds["max_lng"] = max(self.bounds["max_lng"], node.lng)

	def coords_print(self) :
		print 'Running nodes_print()'
		for node in self.nodes :
			print str(self.nodes[node].id) + '\t' + str(self.nodes[node].lng) + '\t' + str(self.nodes[node].lat)
	
	def return_nodes(self) :
		return self.nodes

	def return_node_refs(self) :
		# return a list of all node ids
		node_refs = dict()

		# use an own iterator
		it = 0
		for node in self.nodes.values() :
			node_refs[it] = node.id
			it += 1

		return node_refs


class Road:
	def __init__(self, id, tag, nodes):
		self.id = id						# osm id from file
		self.tag = tag
		self.nodes = nodes			# list of nodes id

class StoreRoads:
	def __init__(self, osmfile):
		# parse the input file and save its contents in memory
		# road ids and node refs as returned from imposm
		self.roads = dict()

		p = OSMParser(ways_callback = self.ways_callback)
		p.parse(osmfile)
	
	# callback function for imposm 
	def ways_callback(self, ways) :
		for osmid, tags, refs in ways :
			road = Road(osmid, tags, refs)
			self.roads[osmid] = road

	def print_roads(self) :
		for road in self.roads :
			print str(self.roads[road].id) + '\t' + str(self.roads[road].tag) + '\n' + str(self.roads[road].nodes) + '\n\n'

	def return_waypoints(self, defined_nodes) :
		# return all nodes that all roads contain that are in the
		# area that ClipNodes defines

		node_refs = dict()
		for road in self.roads.values() :
			# check whether road or not
			if 'highway' in road.tag:
				# get all nodes that the road contains
				node_refs[road] = road.nodes

		nodes = dict()
		for roadkey, road in node_refs.items() :
			nodes[roadkey] = dict()
			for node in road :
				# must check if node is in define_nodes, since the 
				# whole road may not be in the area ClipNodes defines
				if node in defined_nodes :
					nodes[roadkey][node] = defined_nodes[node]

		return nodes

	def return_edges(self, defined_nodes):
		# return all existing edges between nodes that the roads 
		# define

		edges = dict()
		# edges will have it's own iterator
		it = 0

		for road in self.roads.values() :
			# b.index is equal to a.index+1
			# loop from the first node to the second last node
			for a, b in zip(road.nodes, road.nodes[1:]):
				# must check if node is in define_nodes, since the 
				# whole road may not be in the area ClipNodes defines
				if a in defined_nodes and b in defined_nodes :
					edges[it] = Edge(a, b)
					
					# calculate the distance (weight) between node a and b

					edges[it].update_weight(length_haversine(defined_nodes[a], defined_nodes[b])) 
					
					# increment the iterator for edges
					it+=1

		return edges

