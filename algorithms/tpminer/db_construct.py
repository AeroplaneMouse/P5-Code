from tpmmodels.DB import DB


def db_construct(db_a, a_p):
	temp_seq = DB(a_p)

	prfx_starting_ep = find_prfx_s_ep(a_p)

	db_a_p = create_db_a_p(db_a, a_p)
	print(len(db_a_p.ES))
	for cs in db_a_p.ES:
		postfix_prune(cs, a_p, prfx_starting_ep)
		temp_seq.ES.append(cs)

	return temp_seq

def find_prfx_s_ep(prfx):
	s_ep = list(filter(lambda x : x.IsStart, prfx))
	f_ep = list(filter(lambda x : not x.IsStart, prfx))
	print(s_ep)
	print(f_ep)


	for f in f_ep:
		i = 0
		while f.Label != s_ep[i].Label:
			i += 1
		del s_ep[i]
		
	return s_ep

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
