

def point_pruning(FE, a, s_ep):
	for s in FE:
		if not s.IsStart:
			for s_ in s_ep:
				if s.Label == s_.Label:
					break
			else:
				FE.remove(s)

	return FE
