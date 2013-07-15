#simple node class
class Node:
	def __init__(self, id, lng, lat) :
		self.id = id
		self.lng = lng
		self.lat = lat

class Edge:
	def __init__(self, f, t) :
		# f and t are node ids from node f to t 
		self.f = f
		self.t = t
		# w is the weight of the edge
		self.w = None

	def update_weight(self, w) :
		if self.w is None :
			self.w = w
		else :
			# Dont replace a shorter road with a longer one
			# in case of two or more roads between the same nodes
			self.w = min(w, self.w)
