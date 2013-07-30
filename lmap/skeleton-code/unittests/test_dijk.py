import unittest
import sys
sys.path.append("..")

import dijkstra
from graph import Node, Edge, AdjList

class TestDijkstraAdjList(unittest.TestCase) :
	def test_connected_graph_one_path(self) :
		graph = get_graph_connected_one_path()
		shortest_path = dijkstra.adjlist(graph.get_list(), 0, 3)
		self.assertEqual(shortest_path['dist'], 2)
		self.assertEqual(shortest_path['path'], [0, 1, 3])
	def test_disconnected_graph(self) :
		graph = get_graph_disconnected()
		shortest_path1 = dijkstra.adjlist(graph.get_list(), 0, 4)
		shortest_path2 = dijkstra.adjlist(graph.get_list(), 0, 2)
		shortest_path3 = dijkstra.adjlist(graph.get_list(), 3, 4)
		self.assertEqual(shortest_path1, None)
		self.assertEqual(shortest_path2['dist'], 1)
		self.assertEqual(shortest_path2['path'], [0, 2])
		self.assertEqual(shortest_path3['dist'], 1)
		self.assertEqual(shortest_path3['path'], [3, 4])
	def test_no_edges(self) :
		graph = get_graph_no_edges()
		shortest_path = dijkstra.adjlist(graph.get_list(), 0, 2)
		self.assertEqual(shortest_path, None)
	def test_start_or_end_nodes_is_undef(self) :
		graph = get_graph_connected_one_path()
		shortest_path1 = dijkstra.adjlist(graph.get_list(), 0, 4)
		shortest_path2 = dijkstra.adjlist(graph.get_list(), 4, 0)
		shortest_path3 = dijkstra.adjlist(graph.get_list(), -1, -2)
		self.assertEqual(None, shortest_path1)
		self.assertEqual(None, shortest_path2)
		self.assertEqual(None, shortest_path3)
	def test_multiple_ways_between_same_nodes(self) :
		graph = get_graph_multiple_edges_same_nodes()
		shortest_path = dijkstra.adjlist(graph.get_list(), 0, 1)
		self.assertEqual(shortest_path['dist'], 1)

class TestDijkstraAdjMat(unittest.TestCase) :
	def test_connected_graph(self) :
		pass
	def test_disconnected_graph(self) :
		pass
	def test_empty_graph(self) :
		pass
	def test_start_or_end_nodes_is_undef(self) :
		pass
	def test_multiple_ways_between_same_nodes(self) :
		pass


def get_graph_connected_one_path() :
	nodes = dict()
	edges = dict()
	nodes[0] = Node(0, None, None)
	nodes[1] = Node(1, None, None)
	nodes[2] = Node(2, None, None)
	nodes[3] = Node(3, None, None)
	edges[0] = Edge(0, 1, 1)
	edges[1] = Edge(0, 3, 4)
	edges[2] = Edge(1, 2, 1)
	edges[3] = Edge(1, 3, 1)
	edges[4] = Edge(2, 3, 1)
	graph = AdjList(nodes, edges)
	return graph

def get_graph_disconnected() :
	nodes = dict()
	edges = dict()
	nodes[0] = Node(0, None, None)
	nodes[1] = Node(1, None, None)
	nodes[2] = Node(2, None, None)
	nodes[3] = Node(3, None, None)
	nodes[4] = Node(4, None, None)
	edges[0] = Edge(0, 1, 1)
	edges[1] = Edge(0, 2, 1)
	edges[2] = Edge(1, 2, 1)
	edges[3] = Edge(3, 4, 1)
	graph = AdjList(nodes, edges)
	return graph

def get_graph_no_edges() :
	nodes = dict()
	edges = dict()
	nodes[0] = Node(0, None, None)
	nodes[1] = Node(1, None, None)
	nodes[2] = Node(2, None, None)
	graph = AdjList(nodes, edges)
	return graph

def get_graph_multiple_edges_same_nodes() :
	nodes = dict()
	edges = dict()
	nodes[0] = Node(0, None, None)
	nodes[1] = Node(1, None, None)
	edges[0] = Edge(0, 1, 2)
	edges[1] = Edge(0, 1, 1)
	graph = AdjList(nodes, edges)
	return graph


if __name__ == '__main__' :
	unittest.main()




