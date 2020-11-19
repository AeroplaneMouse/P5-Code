from models.IndexSet import IndexSet
from models.IndexRecord import IndexRecord
from algorithms.armada import Storage


# Range set is an index set.
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
