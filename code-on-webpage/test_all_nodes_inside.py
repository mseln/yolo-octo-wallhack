def test_all_nodes_inside(self):
    nodes = NodeSet()
    nodes.add(1, (-10, -10))
    nodes.add(2, (-5, -5))
    selected_nodes = select_nodes_in_rectangle(nodes, -10, 10, -10, 10)

    self.assertTrue(nodes.nodes.keys() == selected_nodes.nodes.keys())
