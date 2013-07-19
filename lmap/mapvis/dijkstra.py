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

def adjlist(G, s, e) :
	# test if start and end nodes is defined and in G
	if e not in G.keys() or s not in G.keys() :
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
		
		for neighboor in G[ind] :
			if W[neighboor[0]] > W[ind] + neighboor[1] :
				W[neighboor[0]] = W[ind] + neighboor[1]
				P[neighboor[0]] = ind

		Q.remove(ind)
		if ind == e :
			break

	S = []
	u = e
	while u in P :
		S += [u]
		u = P[u]
	S += [s]
	S.reverse()

	shortest_path = dict()
	shortest_path['path'] = S
	shortest_path['dist'] = W[e]

	return shortest_path
