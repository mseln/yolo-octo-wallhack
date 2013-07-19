INF = 1000000000

class NodeError(Exception): pass
class OutOfRangeError(NodeError): pass

class Node:
	def __init__(self, id, lng, lat) :
		if not -180 <= lng <= 180 or not -90 <= lat <= 90 :
			# Make it possible to create nodes with undefined coordinates
			if lat is not None and lng is not None :
				raise OutOfRangeError
		self.id = id
		self.lng = lng
		self.lat = lat

class Edge:
	def __init__(self, f, t, w=None) :
		# f and t are node ids from node f to t 
		self.f = f
		self.t = t
		# w is the weight of the edge
		self.w = w

	def update_weight(self, w) :
		if self.w is None :
			self.w = w
		else :
			# Dont replace a shorter road with a longer one
			# in case of two or more roads between the same nodes
			self.w = min(w, self.w)

class AdjMatrix:
	def __init__(self, node_refs, nodes, edges):
		self.node_refs = node_refs
		self.dist = dict()
		# initialize a matrix and fill the diagonal with zeroes and the rest with infinity
		for i in self.node_refs.values() :
			self.dist[i] = dict()
			for j in self.node_refs.values() :
				if i == j :
					self.dist[i][j] = 0
				else :
					self.dist[i][j] = INF
		
		# go through all edges and update the distance between i.f and i.t with i.w
		# initializing both dist[i.f][i.t] and dist[i.t][i.f] with the same value since
		# the distance is the same whether you go in one direction or the other
		for i in edges.values() :
			self.dist[i.f][i.t] = i.w
			self.dist[i.t][i.f] = i.w

	def get_matrix(self) :
		return self.dist

	def print_adjmat_to_file(self, f_name) :
		# write the whole adjency matrix to the file adj_mat.txt
		txt_f = open(f_name,'w')
		for i in self.dist.values() :
			for j in i.values() :
				txt_f.write(str(j) + '\t')
			txt_f.write('\n')
		txt_f.close()

class AdjList :
	def __init__(self, nodes, edges) :
		self.n = dict()
		for node in nodes.values() :
			self.n[node.id] = []

		for edge in edges.values() :
			self.n[edge.t].append([edge.f, edge.w])
			self.n[edge.f].append([edge.t, edge.w])

	def get_list(self) :
		return self.n
