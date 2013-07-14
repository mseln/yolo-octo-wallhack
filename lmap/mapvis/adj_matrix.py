from haversine import length_haversine

INF = 1000000000

class AdjMatrix:
	def __init__(self, node_refs, nodes, edges):
		self.dist = dict()
		for i in node_refs.values() :
			self.dist[i] = dict()
			for j in node_refs.values() :
				self.dist[i][j] = INF

		for i in edges.values() :
			dist = length_haversine(nodes[i.f], nodes[i.t])
			self.dist[i.f][i.t] = dist
			self.dist[i.t][i.f] = dist

	def print_adjmat(self) :
		txt_f = open('adj_mat.txt','w')
		for i in self.dist.values() :
			for j in i.values() :
				txt_f.write(str(j) + '\t')
			txt_f.write('\n')
		txt_f.close()


