def extract_osm_edges(f_name):
    # Parse the supplied OSM file
    parser = make_parser()
    obj = GetRoutes()
    parser.setContentHandler(obj)
    parser.parse(f_name)

    edge_set = None

    # Fill in the missing code
    # pssst osm_parser.py has a function called get_edges()
    # print what that function returns

    return edge_set
