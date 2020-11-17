from tpmmodels.DB import DB


def db_construct(db_a, a_p):
	temp_seq = DB(a_p)

	db_a_p = create_db_a_p(db_a, a_p)

	for cs in db_a_p.ES:
		postfix_prune(cs, a_p)
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

def postfix_prune(cs, a_p):
	for ep in cs:
		if ep.IsStart == False:
			ep.Prune = True
			for a in a_p:
				if ep.Label == a.Label and a.IsStart:
					ep.Prune = False
	prune(cs)

def prune(cs):
	for ep in cs:
		if ep.Prune == True:
			cs.remove(ep)

#Not currently in use
def postfix_prune_old(cs, a_p):
	counter = 0
	for ep in cs:
		counter += 1
		if ep.IsStart == False:
			ep.Prune = True
			for i in range(counter):
				if cs[i].Label == ep.Label and cs[i].IsStart == True:
					ep.Prune = False
	prune(cs)