from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps


#def point_pruning(FE, a, lone_eps):
def point_pruning(FE, a):

	temp_points = set()

	lone_eps = remove_corresponding_eps(a)

	for s in FE:
		if s.IsStart == False:
			for s_ep in lone_eps:
				if s.Label == s_ep.Label and s_ep.IsStart == True:
					temp_points.add(s)
					break
		else:
			temp_points.add(s)
	return temp_points
