from models.IndexSet import IndexSet
from models.IndexRecord import IndexRecord
from algorithms.armada import Storage


# range set is an index set.
def CreateIndexSet(stem, pattern, range_set):
    p_m_idx = IndexSet(pattern, [])

    # Get references to client sequences from MDB or index set
    csList = []
    isIndexSet = False
    if range_set == Storage.MDB:
        csList = Storage.MDB
        start_pos = 0
    else:
        isIndexSet = True
        for record in range_set.Records:
            cs = Storage.MDB[record.Ref]
            csList.append(cs)

    # Goes through all the client sequences in range_set
    i = -1
    for cs in csList:
        i += 1
        # Set starting pos from index record
        if isIndexSet:
            start_pos = range_set.Records[i].Pos + 1

        # Goes through the frequent states in cs
        for pos in range(start_pos, len(cs)):
            # If the state found is equal the index set pattern add to indexSet
            if cs.iloc[pos].State == stem.State:
                ref = i
                intv = [[cs.iloc[pos].Start, cs.iloc[pos].End]]

                new_rec = IndexRecord(pos, intv, ref)
                p_m_idx.Records.append(new_rec)

                # Break when the first occurrence of the state is found
                break

    return p_m_idx


def printPatterns():
    # for i in range(len(patterns)):
    #     print("Pattern nr: " + str(i))
    #     print(patterns[i])
    #     print()
    print('Patterns: {}'.format(len(patterns)))


"""
# MDB is the list of client sequences
# visited_states is used to keep check of frequent states that already have an index set
def CreateFirstIndexSet(stem, visited_states):
    idx = IndexSet(CreatePattern(None, stem.State), [])
    #Checks if a index set is already created
    if stem.State not in visited_states:
        visited_states.append(stem.State)
        #Goes through all the client sequences in mdb
        for cs in Storage.MDB:
            #goes through the frequent states in cs
            for singleState in range(0,len(cs)):
                #if the state found is equal the index set pattern add to index set
                if cs.iloc[singleState].State == stem.State:
                    
                    ref = cs
                    intv = [[cs.iloc[singleState].Start, cs.iloc[singleState].End]]
                    pos = singleState

                    new_rec = IndexRecord(pos, intv, ref)

                    idx.Records.append(new_rec)
                    break
            continue
        return idx
"""