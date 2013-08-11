import sys
from datetime import datetime

from xml.sax import make_parser
from mapvis.osm_parser import GetRoutes

# Parse the supplied OSM file
obj = GetRoutes()
parser = make_parser()
parser.setContentHandler(obj)

print("Parsing data...")
start = datetime.now()
parser.parse(sys.argv[1])
end = datetime.now()
print("Done! " + str((end-start).total_seconds()) + " (s)")

print("Data is containing " + str(len(obj.nodes)) + " nodes")