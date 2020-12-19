
#uses the list of frequent endpoints (FE) returned by count_support and a list of starting endpoints.
#to recursively prune away points (endpoints) that will never become part of a pattern such as (D+ E-) for prefix D+
#since E+ has to come before E- and we are not looking before D+ occurs
def point_pruning(FE, a, s_ep):
	FE_pruned = set()

	for s in FE:
		if s.IsStart:
			FE_pruned.add(s)
		else:
			for s_ in s_ep:
				if s.Label == s_.Label:
					FE_pruned.add(s)
					break

	return FE_pruned
