# A simple node class
from xml.sax import make_parser, handler
from .osm_parser import GetRoutes

from .algorithms import length_haversine

class Node:
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat
        self.lng = lng
        

class NodeSet:
    def __init__(self):
        self.nodes = dict()
 
        # actual min and max latitude and longitude of coordinates
        self.bounds = dict()
        self.bounds["min_lat"] = 90
        self.bounds["max_lat"] = -90
        self.bounds["min_lng"] = 180
        self.bounds["max_lng"] = -180
 
    def add(self, id, node):
        lat = node[0]
        lng = node[1]
 
        self.nodes[id] = Node(id, lat, lng)
        self.bounds["min_lat"] = min(self.bounds["min_lat"], lat)
        self.bounds["min_lng"] = min(self.bounds["min_lng"], lng)
        self.bounds["max_lat"] = max(self.bounds["max_lat"], lat)
        self.bounds["max_lng"] = max(self.bounds["max_lng"], lng)
 
    def remove(self, id):
        del self.nodes[id]
 
    def return_nodes(self):
        return self.nodes
 
    def print_node_set(self):
        print("Printing NodeSet")
        for k, n in self.nodes.items():
            print("id:" + str(k) + "\tlat: " + str(n.lat) +
                  "\tlng:" + str(n.lng))

    def get_nodes_in_pairs(self, edges):
        pair_list = []
        for edge in edges:
            pair_list += [[self.nodes[edge[0]],
                           self.nodes[edge[1]]]]
        return pair_list


class Edge:
    def __init__(self, f, t, w=None):
        # f and t are node ids from node f to t
        self.f = f
        self.t = t
        # w is the weight of the edge
        self.w = w

    def update_weight(self, w):
        if self.w is None:
            self.w = w
        else:
            # Don't replace a shorter road with a longer one
            # in case of two or more roads between the same nodes
            self.w = min(w, self.w)

class EdgeSet:
    def __init__(self):
        self.edges = []


    def add(self, f, t, w=None):
        self.edges += [Edge(f, t, w)]

    def print_edge_set(self):
        for k, n in self.edges.items():
            print("id:" + str(k) + "\tneighboors: " + str(n))

    def return_edges(self):
        return self.edges

    def get_edges(self):
        edges = []
        for edge in self.edges:
            edges += [(edge.f, edge.t)]
        return edges

class AdjMat:
    def __init__(self, nodes, edges):
        self.dist = dict()
        # initialize a matrix and fill the diagonal with zeroes and the rest with infinity
        for i in nodes.keys() :
            self.dist[i] = dict()
            for j in nodes.keys() :
                if i == j :
                    self.dist[i][j] = 0
                else :
                    self.dist[i][j] = float('inf')
        
        # go through all edges and update the distance between i.f and i.t with i.w
        # initializing both dist[i.f][i.t] and dist[i.t][i.f] with the same value since
        # the distance is the same whether you go in one direction or the other
        # print(edges)
        for i in edges :
            self.dist[i.f][i.t] = i.w
            self.dist[i.t][i.f] = i.w

    def return_matrix(self):
        return self.dist

    def print_adjmat_to_file(self, f_name) :
        # Write the whole adjacency matrix to the file which is given as f_name
        # This was the easiest way two display a somewhat big matrix in a readable way.
        txt_f = open(f_name,'w')
        for i in self.dist.values() :
            for j in i.values() :
                txt_f.write('%.2f\t' %  j)
            txt_f.write('\n')
        txt_f.close()


def extract_osm_nodes(f_name):
    # Parse the supplied OSM file
    # print("Loading data...")
    obj = GetRoutes()
    parser = make_parser()
    parser.setContentHandler(obj)
    
    # print("Parsing nodes!")
    parser.parse(f_name)
    # print("Done!")

    nodes = obj.get_nodes()
    node_set = NodeSet()
    for k, n in nodes.items():
        node_set.add(k, n)
 
    return node_set

def select_nodes_in_rectangle(nodes, min_lat, max_lat, min_lng, max_lng):
    # actual min and max latitude and longitude of coordinates

    nodes_in_rectangle = NodeSet()
    for k, node in nodes.return_nodes().items():
        if(min_lat <= node.lat and node.lat <= max_lat and 
           min_lng <= node.lng and node.lng <= max_lng):
            nodes_in_rectangle.add(k, (node.lat, node.lng))
 
    return nodes_in_rectangle

def extract_osm_edges(f_name, nodes):
    valid_nodes = list(nodes.keys())

    # Parse the supplied OSM file
    # print("Loading data...")
    obj = GetRoutes()
    parser = make_parser()
    parser.setContentHandler(obj)
    
    # print("Parsing edges!")
    parser.parse(f_name)
    # print("Done!")

    edges = obj.get_edges()
    for k, n in edges.items():
        # print("id:" + str(k) + "\tneighboors: " + str(n))
        pass
    edge_set = EdgeSet()
    it = 0
    for k, n in edges.items():
        for m in n:
            if k in valid_nodes and m in valid_nodes:
                edge_set.add(k, m, length_haversine(nodes[k], nodes[m]))
                it += 1

    return edge_set