INF = 1000000000

def print_adjmat(G) :
	# write the whole adjency matrix to the file adj_mat.txt
	txt_f = open('adj_mat.txt','w')
	for i in G.values() :
		for j in i.values() :
			txt_f.write(str(j) + '\t')
		txt_f.write('\n')
	txt_f.close()

def dijkstra(G, s, e) :
	print_adjmat(G)
	# Q = dict()
	Q = G.keys()
	
	W = dict()
	T = dict()
	P = dict()
	for i in Q :
		W[i] = INF
		T[i] = False
	W[s] = 0

	#for i in W :
		#print str(i) + ' ' + str(W[i])
	#print Q
	while Q :
		m = INF+1
		ind = None

		# print 'new round! \n\n'
		for i in W :
			# print str(i) + ' ' + str(W[i]) + ' ' + str(ind) + ' ' + str(T[i])
			if W[i] < m and not T[i]:
				m = W[i] 
				ind = i
		
		for i in Q :
			# print str(i) + ' ' + str(W[i]) + ' ' + str(G[ind][i])
			# alt = INF
			# if G[ind][i] not INF :
				# alt = W[ind] + G[ind][i]
			if W[i] > W[ind] + G[i][ind] :
				W[i] = W[ind] + G[i][ind]
				P[i] = ind


		T[ind] = True
		Q.remove(ind)
		if ind == e :
			break

	print W[e]

	
	S = []
	u = e
	while u in P :
		S += [u]
		u = P[u]
	S += [s]
	S.reverse()
	
	return S
