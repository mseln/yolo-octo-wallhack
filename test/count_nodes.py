from imposm.parser import OSMParser
# simple class that handles the parsed OSM data .
class NodeCounter(object) :
	counter = 0
	# callback method for coords
	def count(self, coords):
		self.counter += len (coords)
	
# instantiate counter and parser and start parsing
nodes = NodeCounter()
p = OSMParser(coords_callback = nodes.count)
p.parse('map.osm')
# done
print nodes.counter
