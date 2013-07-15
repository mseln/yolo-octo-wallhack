from math import sqrt , radians , sin , cos , asin
INF = 1000000000

def length_haversine(p1, p2) :
	# calculate distance using the haversine formula ,
	# which incorporates earth curvature
	# see http ://en.wikipedia.org/wiki/Haversine_formula
	lat1 = p1.lat
	lng1 = p1.lng
	lat2 = p2.lat
	lng2 = p2.lng
	lat1, lng1, lat2, lng2 = map(radians , [lat1, lng1, lat2, lng2])
	dlng = lng2 - lng1
	dlat = lat2 - lat1
	a = sin( dlat/2 ) ** 2 + cos(lat1) * cos(lat2) * sin(dlng/2) ** 2
	c = 2 * asin(sqrt(a))
	return 6372797.560856 * c # return distance in m

def find_closest_node(pos, nodes) :
	min_d = INF
	best_node = None

	# simple linear search
	for nodekey, node in nodes.items() :
		d = length_haversine(pos, node)
		if min_d > d:
			min_d = d
			best_node = nodekey
	
	return best_node

