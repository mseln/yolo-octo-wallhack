def select_nodes_in_rectangle(nodes, min_lat, max_lat, min_lng, max_lng):
    # actual min and max latitude and longitude of coordinates
    nodes_in_rectangle = NodeSet()
    for k, node in nodes.get_nodes().items():
        if(min_lat <= node.lat and node.lat and
           min_lng <= node.lng and node.lng):
            nodes_in_rectangle.add(k, (node.lat, node.lng))

    return nodes_in_rectangle
