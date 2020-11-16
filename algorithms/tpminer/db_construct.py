

#a_p is a single character
def db_construct(db_a, a_p):
	temp_seq = []

	db_a_p = create_db_a_p(db_a, a_p)

	for cs in db_a_p:
		postfix_prune(cs)
		temp_seq.append(cs)


def create_db_a_p(db_a, a_p):
	db_a_p = []

	for cs in db_a:
		counter = 0
		for ep in cs:
			counter += 1
			if ep.Label == a_p:
				db_a_p.append(cs[counter:])
	return db_a_p

def postfix_prune(cs):
	counter = 0
	for ep in cs:
		counter += 1
		if ep.IsStart == False:
			ep.Prune = True
			for i in range(counter):
				if cs[i].Label == ep.Label and cs[i].IsStart == True:
					ep.Prune = False
	prune(cs)

def prune(cs):
	for ep in cs:
		if ep.Prune == True:
			cs.remove(ep)
	print(cs)
