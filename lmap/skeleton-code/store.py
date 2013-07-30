from imposm.parser import OSMParser
from my_func import length_haversine
import graph

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
			node = graph.Node(osmid ,lng ,lat)
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
			if self.minlng <= node.lng and node.lng <= self.maxlng and self.minlat <= node.lat and node.lat <= self.maxlat :
				new_node = graph.Node(node.id, node.lng, node.lat)
				self.nodes[node.id] = node

				# update bounds
				self.bounds["min_lat"] = min(self.bounds["min_lat"], node.lat)
				self.bounds["min_lng"] = min(self.bounds["min_lng"], node.lng)
				self.bounds["max_lat"] = max(self.bounds["max_lat"], node.lat)
				self.bounds["max_lng"] = max(self.bounds["max_lng"], node.lng)

	# Good idea to make a function that outputs (id, lat, lng)
	# of every node for debugging purposes?
	def coords_print(self) :

	def return_nodes(self) :
		return self.nodes

class Road:
	def __init__(self, id, tag, nodes):
		self.id = id				# osm id from file
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
		pass

	# Good idea to make a function that outputs (id, lat, lng)
	# of every node the road contains for debugging purposes?
	def print_roads(self) :
		pass