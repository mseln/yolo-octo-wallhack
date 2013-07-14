#simple node class
class Node:
	def __init__(self, id, lng, lat):
		self.id = id
		self.lng = lng
		self.lat = lat

class Edge:
	def __init__(self, f, t):
		self.f = f
		self.t = t

