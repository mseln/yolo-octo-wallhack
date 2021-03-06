import random
import unittest
import sys
sys.path.append("..")

import graph

class TestNodes(unittest.TestCase) :
	def test_outside(self) :
		nodes = dict()
		self.assertRaises(graph.OutOfRangeError, graph.Node, 1, 181, 0)
		self.assertRaises(graph.OutOfRangeError, graph.Node, 1, 181, 0)
		self.assertRaises(graph.OutOfRangeError, graph.Node, 1, 181, 0)
		self.assertRaises(graph.OutOfRangeError, graph.Node, 1, 181, 0)
	def test_random(self) :
		nodes = dict()
		for i in range(100) :
			lat = random.randint(-180, 180)
			lng = random.randint(-360, 360)
			if not -90 <= lat <= 90 or not -180 <= lng <= 180 :
				self.assertRaises(graph.OutOfRangeError, graph.Node, i, lng, lat)
		
if __name__ == '__main__' :
	unittest.main()
