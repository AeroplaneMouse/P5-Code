from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps


def point_pruning(FE, a):
	
	prfx_starting_ep = remove_corresponding_eps(a)

	temp_points = set()

	for s in FE:
		if s.IsStart == False:
			for s_ep in prfx_starting_ep:
				if s.Label == s_ep.Label and s_ep.IsStart == True:
					temp_points.add(s)
					break
		else:
			temp_points.add(s)
	return temp_points
