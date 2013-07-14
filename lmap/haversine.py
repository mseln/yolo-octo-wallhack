from math import sqrt , radians , sin , cos , asin

def length_haversine ( p1 , p2 ) :
	# calculate distance using the haversine formula ,
	# which incorporates earth curvature
	# see http :// en . wikipedia . org / wiki / Haversine_formula
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

