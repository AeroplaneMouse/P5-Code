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
    for i in range(0, len(flags)):
        flags[i] = False


def ComputePotentialStems(indexSet, frequentStates, cs):
    stems = []
    counts = []
    flags = []

    # Check every record in indexSet
    for record in indexSet.Records:
        csRef = record.Ref
        ResetFlags(flags)

        # Go through every cs after reference from IndexRecord
        for i in range(csRef + 1, len(cs)):
            singleCS = cs.iloc[i]

            # Check if cs state is a frequentState
            if singleCS.State in frequentStates:
                # Update state count if not done for current record
                if singleCS.State in stems:
                    index = stems.index(singleCS.State)
                    if not flags[index]:
                        counts[index] += 1
                        flags[index] = True
                # Add state as new stem
                else:
                    stems.append(singleCS.State)
                    counts.append(1)
                    flags.append(True)

    # Remove shit stems
    # for i in range(0, len(stems)):
    #   if count[i] < 0:

    return stems


def MineIndexSet(pattern, indexSet, frequentStates, cs):
    stems = ComputePotentialStems(indexSet, frequentStates, cs)
    print(stems)

    import pdb; pdb.set_trace()  # breakpoint b90b85f2 //

    rSet = []
    prefix = None  # Mock
    for s in stems:
        p = CreatePattern(prefix, s)
        iSet = CreateIndexSet(s, p, rSet)
        MineIndexSet(p, iSet)
