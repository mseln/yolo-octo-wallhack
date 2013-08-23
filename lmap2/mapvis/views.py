from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
import datetime
 
from .road_network import RoadNetwork

def hello(request):
    now = datetime.datetime.now()
    html = "<html><body>Hello world! It is now %s.</body></html>" % now
    return HttpResponse(html)
 

def mapapp(request):    
    road_network = RoadNetwork()
    edges = road_network.return_edges()
    nodes = road_network.return_nodes()

    c = Context({'GMAPS_API_KEY': 'AIzaSyDUVb0C40shGs7dL4jC9pdCeBNUDlrt4YA',
                 'COORDS': nodes,
                 'EDGES': edges})
    return render_to_response('mapvis/mapapp.html', c)