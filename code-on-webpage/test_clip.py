import random
import unittest
from nodes import *

def node_inside(node, min_lat, max_lat, min_lng, max_lng):
    return (min_lat <= node.lat and node.lat <= max_lat
            and min_lng <= node.lng and node.lng <= max_lng)

class TestClipNodes(unittest.TestCase):

    def test_empty_nodes(self):
        nodes = dict()
        selected_nodes = ClipNodes(nodes, -10, 10, -10, 10)
        self.assertEqual(nodes, selected_nodes.nodes)
        
    def test_empty_clip_nodes(self):
        nodes = dict()
        nodes[1] = Node(1, -10, -10)
        nodes[2] = Node(2, -5, -5)
        selected_nodes = ClipNodes(nodes, 0, 10, 0, 10)
        self.assertFalse(selected_nodes.nodes)

    #def test_some_nodes_inside(self):

    #def test_all_nodes_inside(self):

    def test_random(self):
        # Create 100 random nodes
        nodes = dict()
        for i in range(100):
            node = Node(i, random.randint(-180, 180), 
                           random.randint(-90, 90))
            nodes[i] = node

        # Randomly choose the min and max latitude and longitude
        min_lat = random.randint(-90, 90)
        min_lng = random.randint(-180, 180)
        max_lat = min_lat + random.randint(0, 90-min_lat)
        max_lng = min_lng + random.randint(0, 180-min_lng)
        
        # Extract all nodes within the randomly generated rectangle
        selected_nodes = ClipNodes(nodes, min_lat, max_lat, 
                                   min_lng, max_lng)

        # Make sure that all nodes that should be inside are inside
        for n in nodes.values():
            if n in selected_nodes.nodes.values():
                self.assertTrue(node_inside(n, min_lat, max_lat, 
                                            min_lng, max_lng))
            else:
                self.assertFalse(node_inside(n, min_lat, max_lat, 
                                             min_lng, max_lng))
                
if __name__ == '__main__':
    unittest.main()