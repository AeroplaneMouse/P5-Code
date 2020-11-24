from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
from tpmmodels.Ep_sup import Ep_sup

def count_support(db_a, min_sup):

	prfx_trimmed = remove_corresponding_eps(db_a.Pattern)
	FE = []

	for cs in db_a.ES:
		j = find_stop_pos(cs, prfx_trimmed)
		acc_sup(cs[:j+1], FE)

	cs_n = len(db_a.ES)
	for ep in FE:
		if ep.Support / cs_n < min_sup:
			FE.remove(ep)

	return FE

def find_stop_pos(cs, prfx_s_ep):
	if len(prfx_s_ep) > 0:
		i = 0
		while not is_stop_ep(cs[i], prfx_s_ep):
			i += 1
		p = cs[i].Parenthesis
		if p > 0:
			while cs[i + 1].Parenthesis == p:
				i += 1
		return i
	else:
		return len(cs) - 1

def is_stop_ep(ep, prfx_s_ep):
	if not ep.IsStart:
		for s_ep in prfx_s_ep:
			if ep.Label == s_ep.Label:
				return True
		return False
	else:
		return False


def acc_sup(cs, suppList):
	for ep in cs:
		is_in_list = False
		for i in range(len(suppList)):
			if ep.Label == suppList[i].Label and ep.IsStart == suppList[i].IsStart:
				suppList[i].Support += 1
				is_in_list = True
		if not is_in_list:
			suppList.append(Ep_sup(ep.Label, ep.IsStart, 1))
