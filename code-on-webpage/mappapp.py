def mapapp(request):
    node_set = extract_osm_nodes("liu.osm")
    node_set = select_nodes_in_rectangle(node_set,
                                         58.3984, 58.3990,
                                         15.5733, 15.576)
    c = Context({'GMAPS_API_KEY': 'YOUR_GMAPS_API_KEY',
                 'COORDS': node_set.get_nodes().values()},)
