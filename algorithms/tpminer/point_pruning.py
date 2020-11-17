

def point_pruning(FE, a):
	temp_points = []

	for s in FE:
		if s.IsStart == False:
			for ep in a:
				if s.Label == ep.Label and ep.IsStart == True:
					temp_points.append(s)
					break
		else:
			temp_points.append(s)
	return temp_points
