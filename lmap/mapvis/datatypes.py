# A simple road class
class Road:
	def __init__(self, id, nodes):
		self.id = id						# osm id from file
		self.nodes = nodes			# list of nodes id

class StoreRoads:
	def __init__(self, osmfile):
		# parse the input file and save its contents in memory

		# road ids and node refs as returned from imposm
		self.roads = dict()

		p = OSMParser(ways_callback = self.ways_callback)
		p.parse(osmfile)

	def ways_callback(self, ways)
		# fill in the missing code

