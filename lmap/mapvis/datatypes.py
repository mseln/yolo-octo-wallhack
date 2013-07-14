# A simple road class

from node import Node
from imposm.parser import OSMParser

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
	
	def ways_callback(self, ways) :
		for osmid, tags, refs in ways :
			road = Road(osmid, tags, refs)
			self.roads[osmid] = road

	def print_roads(self) :
		for road in self.roads :
			print str(self.roads[road].id) + '\t' + str(self.roads[road].tag) + '\n' + str(self.roads[road].nodes) + '\n\n'

	def return_waypoints(self, all_nodes) :
		node_refs = dict()
		for road in self.roads :
			if 'highway' in self.roads[road].tag:
				node_refs[road] = self.roads[road].nodes

		nodes = dict()
		for roadkey, road in node_refs.items() :
			nodes[roadkey] = dict()
			for node in road :
					if node in all_nodes :
						nodes[roadkey][node] = all_nodes[node]

		return nodes
