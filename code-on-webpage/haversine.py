from math import sqrt, radians, sin, cos, asin

def length_haversine(p1, p2):
    # calculate the distance between two points using the Haversine
    # formula which incorporates the earth's curvature, see
    # http://en.wikipedia.org/wiki/Haversine_formula.
    lat1 = p1.lat
    lng1 = p1.lng
    lat2 = p2.lat
    lng2 = p2.lng
    lat1, lng1, lat2, lng2 = map(radians, [lat1, lng1, lat2, lng2])
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(a))
    # return the distance in m
    return 6372797.560856 * c  
