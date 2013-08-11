def extract_osm_nodes(f_name):
    # Parse the supplied OSM file
    print("Loading data...")
    obj = GetRoutes()
    parser = make_parser()
    parser.setContentHandler(obj)
    parser.parse(f_name)

    nodes = obj.get_nodes()
    node_set = NodeSet()
    for k, n in nodes.items():
        node_set.add(k, n)

    return node_set
