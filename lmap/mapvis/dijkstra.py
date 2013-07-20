INF = 1000000000

def adjmat(G, s, e) :
	if not e or not s :
		return None

	Q = G.keys()
	W = dict()
	P = dict()
	
	for i in Q :
		W[i] = INF
	W[s] = 0

	while Q :
		m = INF
		ind = None

		for i in W :
			if W[i] < m and i in Q:
				m = W[i] 
				ind = i
		if ind is None : return None
		
		for i in Q :
			if W[i] > W[ind] + G[i][ind] :
				W[i] = W[ind] + G[i][ind]
				P[i] = ind


		Q.remove(ind)
		if ind == e :
			break

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
