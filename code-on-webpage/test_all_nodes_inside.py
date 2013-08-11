def test_all_nodes_inside(self):
    nodes = dict()
    nodes[1] = Node(1, -10, -10)
    nodes[2] = Node(2, -5, -5)
    selected_nodes = ClipNodes(nodes, -10, 10, -10, 10)
    self.assertTrue(nodes == selected_nodes.nodes)
