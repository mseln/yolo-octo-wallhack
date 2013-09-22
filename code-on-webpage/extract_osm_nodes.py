def extract_osm_nodes(f_name):
    # Parse the supplied OSM file
    print("Loading data...")
    parser = make_parser()
    obj = GetRoutes()
    parser.setContentHandler(obj)
    parser.parse(f_name)

    nodes = obj.get_nodes()
    node_set = NodeSet()
    for k, n in nodes.items():
        node_set.add(k, n[0], n[1])

    return node_set
