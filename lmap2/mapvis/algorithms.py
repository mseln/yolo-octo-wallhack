from math import sqrt, radians, sin, cos, asin
INF = 1000000000

def length_haversine(p1, p2) :
    # calculate distance using the haversine formula ,
    # which incorporates earth curvature
    # see http ://en.wikipedia.org/wiki/Haversine_formula
    lat1 = p1.lat
    lng1 = p1.lng
    lat2 = p2.lat
    lng2 = p2.lng
    lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat/2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng/2) ** 2
    c = 2 * asin(sqrt(a))
    return 6372797.560856 * c # return distance in m


# This function takes an adjacency matrix, a start node and
# an end node as parameters. It returns the shortest path and 
# the weight of the shortest path.
# RUNNING TIME O(V^2)


def dijk_adjmat(G, s, e) :
    if not e or not s :
        return None

    Q = list(G.keys())      # A list of all node references.
    W = dict()              # Will be the weight to node W[k] when the algoritm is done.
    P = dict()              # Used to reproduce the path

    # Init set the weight to all nodes to infinity
    # and then the weight to the start node to zero 
    for i in Q :
        W[i] = INF
    W[s] = 0

    while Q :
        m = INF
        ind = None

        # Get the unvisited node with shortest distance from start.
        for i in W :
            if W[i] < m and i in Q:
                m = W[i] 
                ind = i
        # If there aren't one the start is not connected to the end.
        if ind is None : return None
        
        # Relax the edges.
        for i in Q :
            if W[i] > W[ind] + G[i][ind] :
                W[i] = W[ind] + G[i][ind]
                P[i] = ind

        # Mark as visited by removing it.
        Q.remove(ind)
        # if ind == e :
        #    break

    # Reproduce the path.
    S = []
    u = e
    while u in P :
        S += [u]
        u = P[u]
    S += [s]
    
    shortest_path = dict()
    shortest_path['path'] = S
    shortest_path['dist'] = W[e]

    return shortest_path