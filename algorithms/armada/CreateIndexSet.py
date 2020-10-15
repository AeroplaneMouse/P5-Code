from models.IndexSet import IndexSet
from models.IndexRecord import IndexRecord

def CreateIndexSet(stem, prefix, range_set, cs_list, IndexRecord):
    for clientSequence in range_set.Records:
        if range_set == None:
            start_pos = 0
        else:
            start_pos = IndexRecord.Pos
        IndexRecord = start_pos + 1
        for i, IndexRecord in range(cs_list):
            if s in cs_list:
                IndexSet.insert(cs_list[i], "a_intv", start_pos)
    return IndexSet