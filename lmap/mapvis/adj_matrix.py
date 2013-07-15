INF = 1000000000

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

		# calculate all shortest paths between all edges
		self.perform_floyd_warshall()

	def print_adjmat(self) :
		# write the whole adjency matrix to the file adj_mat.txt
		txt_f = open('adj_mat.txt','w')
		for i in self.dist.values() :
			for j in i.values() :
				txt_f.write(str(j) + '\t')
			txt_f.write('\n')
		txt_f.close()

	def perform_floyd_warshall(self) :
		# calculate all the shortest path between all nodes
		# distance between node a and b will be dist[a.index][b.index]
		# since the graph is undirected will dist[a.index][b.index] be the same as dist[b.index][a.index]
		# read about the algorithm: http://en.wikipedia.org/wiki/Floyd-Warshall_algorithm
		for k in self.node_refs.values() :
			for i in self.node_refs.values() :
				for j in self.node_refs.values() :
					self.dist[i][j] = min(self.dist[i][k] + self.dist[k][j], self.dist[i][j])
