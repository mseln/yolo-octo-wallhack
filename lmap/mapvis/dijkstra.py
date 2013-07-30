# Read about dijkstra here: http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# 

INF = 1000000000

# This function takes an adjacency matrix, a start node and
# an end node as parameters. It returns the shortest path and 
# the weight of the shortest path.
# RUNNING TIME O(V^2)
def adjmat(G, s, e) :
	if not e or not s :
		return None

	Q = G.keys()	# A list of all node references.
	W = dict()		# Will be the weight to node W[k] when the algoritm is done.
	P = dict()		# Used to reproduce the path

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
		if ind == e :
			break

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

from heapq import heappush, heappop
def adjlist(G, s, e) :
	# test if start and end nodes is defined and in G
	if e not in G.keys() or s not in G.keys() :
		return None

	N = len(G.keys())
	W = dict()
	P = dict()
	for key in G.keys() : 
		W[key] = INF
		P[key] = None
 	W[s] = 0
 	h = []
 	heappush(h, (0, s))
	for i in range(N - 1):
		min_dist, k = 0, 0
	 	if not h: break
	 	while h:
			min_dist, k = heappop(h)
			if min_dist == W[k]: break
		for j, w in G[k]:
			if W[j] > W[k] + w:
				W[j] = W[k] + w
				P[j] = k
				heappush(h, (W[j], j))
	
	S = []
	u = e
	while u in P :
		S += [u]
		u = P[u]
	S.reverse()
	
	shortest_path = dict()
	shortest_path['path'] = S
	shortest_path['dist'] = W[e]
	return shortest_path
