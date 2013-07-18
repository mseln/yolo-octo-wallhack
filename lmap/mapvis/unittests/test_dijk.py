import unittest
import sys
sys.path.append("..")

import dijkstra
import graph
class TestDijkstraAdjList(unittest.TestCase) :
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

if __name__ == '__main__' :
	unittest.main()
