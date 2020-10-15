# from CreateIndexSet import CreateIndexSet
# from CreatePattern import CreatePattern


#############################################
# Mocks
def CreateIndexSet(one, two, three):
	return

def CreatePattern(prefix, state):
	return

#############################################

def ResetFlags(flags):
	for i in range(0, len(flag)):
		flags[i] = False


def ComputePotentialStems(indexSet):
	stems = []
	counts = []
	flags = []
	
	# 
	for record in indexSet.Records:
		csRef = record.Ref
		ResetFlags(flags)

		for i in range(csRef[record.Pos+1, len(csRef)]):
			
			state = csRef[i].State
			if state in FrequentStates:
				if state in stems:
					index = stems.index(state)
					if not flags[index]:
						counts[index] += 1
						flags[index] = True
				else:
					stems.append([state])
					counts.append(1)
					flags.append(True)
	
	# Remove shit stems
	# for i in range(0, len(stems)):
	# 	if count[i] < 0:


	return stems

def MineIndexSet(pattern, indexSet):
	stems = ComputePotentialStems(indexSet)
	rSet = []

	for s in stems:
		p = CreatePattern(prefix, s)
		iSet = CreateIndexSet(s, p, rSet)
		MineIndexSet(p, iSet)

