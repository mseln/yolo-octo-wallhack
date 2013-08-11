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

        self.nodes[id] = Node(lat, lng)
        self.bounds["min_lat"] = min(self.bounds["min_lat"], lat)
        self.bounds["min_lng"] = min(self.bounds["min_lng"], lng)
        self.bounds["max_lat"] = max(self.bounds["max_lat"], lat)
        self.bounds["max_lng"] = max(self.bounds["max_lng"], lng)

    def remove(self, id):
        del self.nodes[id]

    def get_nodes(self):
        return self.nodes

    def print_node_set(self):
        for k, n in self.nodes.items():
            print("id:" + str(k) + "\tlat: " + str(n.lat) +
                  "\tlng:" + str(n.lng))
