
#uses the list of frequent endpoints (FE) returned by count_support and a list of starting endpoints.
#to recursively prune away points (endpoints) that will never become part of a pattern such as (D+ E-) for prefix D+
#since E+ has to come before E- and we are not looking before D+ occurs
def point_pruning(FE, a, s_ep):
	for s in FE:
		if not s.IsStart:
			for s_ in s_ep:
				if s.Label == s_.Label:
					break
			else:
				FE.remove(s)

	return FE
