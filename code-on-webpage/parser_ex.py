# Parser example
# Usage python parser_ex.py <data.osm>

import sys
from datetime import datetime

from xml.sax import make_parser
from mapvis.osm_parser import GetRoutes

# Parse the supplied OSM file
parser = make_parser()          # Create a parser object 
obj = GetRoutes()               # Create the target of the parser
parser.setContentHandler(obj)   # Set the target

print("Parsing data...")
start = datetime.now()
parser.parse(sys.argv[1])       # Parse the data
end = datetime.now()
print("Done! " + str((end-start).total_seconds()) + " (s)")

print("The data contains " + str(len(obj.nodes)) + " nodes")
