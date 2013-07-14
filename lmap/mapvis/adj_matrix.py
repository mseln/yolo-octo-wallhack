from haversine import length_haversine

INF = 1000000000

class AdjMatrix:
	def __init__(self, node_refs, nodes, edges):
		self.node_refs = node_refs
		self.dist = dict()
		for i in self.node_refs.values() :
			self.dist[i] = dict()
			for j in self.node_refs.values() :
				if i == j :
					self.dist[i][j] = 0
				else :
					self.dist[i][j] = INF
		
		for i in edges.values() :
			dist = length_haversine(nodes[i.f], nodes[i.t])
			self.dist[i.f][i.t] = dist
			self.dist[i.t][i.f] = dist

		self.perform_floyd_warshall()

	def print_adjmat(self) :
		txt_f = open('adj_mat.txt','w')
		for i in self.dist.values() :
			for j in i.values() :
				txt_f.write(str(j) + '\t')
			txt_f.write('\n')
		txt_f.close()

	def perform_floyd_warshall(self) :
		for k in self.node_refs.values() :
			for i in self.node_refs.values() :
				for j in self.node_refs.values() :
					self.dist[i][j] = min(self.dist[i][k] + self.dist[k][j], self.dist[i][j])
