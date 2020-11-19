from tpmmodels.DB import DB
from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps


def db_construct(db_a, a_p):
	temp_seq = DB(a_p)

	prfx_starting_ep = remove_corresponding_eps(a_p)

	db_a_p = create_db_a_p(db_a, a_p)
	print(len(db_a_p.ES))
	for cs in db_a_p.ES:
		postfix_prune(cs, a_p, prfx_starting_ep)
		temp_seq.ES.append(cs)

	return temp_seq

def create_db_a_p(db_a, a_p):
	db_a_p = DB(a_p)
	a_last = a_p[-1]

	for cs in db_a.ES:
		counter = 0
		for ep in cs:
			counter += 1
			if ep.Label == a_last.Label and ep.IsStart == a_last.IsStart:
				db_a_p.ES.append(cs[counter:])
	return db_a_p

def postfix_prune(cs, a_p, s_ep):
	for ep in cs:
		if ep.IsStart == False:
			ep.Prune = True
			for s in s_ep:
				if ep.Label == s.Label:
					ep.Prune = False
					break
			
	prune(cs)

def prune(cs):
	for ep in cs:
		if ep.Prune == True:
			cs.remove(ep)
