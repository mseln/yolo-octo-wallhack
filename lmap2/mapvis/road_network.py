import datetime

from .store import extract_osm_nodes, select_nodes_in_rectangle
from .store import extract_osm_edges
from .store import AdjMat
from .algorithms import dijk_adjmat

class RoadNetwork:
    def __init__(self):
        self.node_set = extract_osm_nodes("linkoping_map.osm")
        self.node_set = select_nodes_in_rectangle(self.node_set,
                                                  58.3900, 58.4050,
                                                  15.5700, 15.5900)
        # node_set.print_node_set()

        self.edge_set = extract_osm_edges("linkoping_map.osm", 
                                          self.node_set.return_nodes())
        # edge_set.print_edge_set()

        all_edges = self.edge_set.get_edges()
        self.pair_list = self.node_set.get_nodes_in_pairs(all_edges)
        # print(pair_list)

        adj_mat = AdjMat(self.node_set.return_nodes(),
                         self.edge_set.return_edges())
        adj_mat.print_adjmat_to_file('adj_mat.txt')

        start = datetime.datetime.now()
        shortest_path = dijk_adjmat(adj_mat.return_matrix(), 81388, 81388)
        end = datetime.datetime.now()

        print("Node set contain " + str(len(self.node_set.return_nodes())) + " nodes")
        print("Dijkstra took " + str(end-start) + " seconds to run")
        # print(shortest_path)

    def return_edges(self):
        return self.pair_list

    def return_nodes(self):
        return self.node_set.return_nodes().values()
