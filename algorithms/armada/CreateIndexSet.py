from models.IndexSet import IndexSet
from models.IndexRecord import IndexRecord
import copy as copy


# range set is an index set.
def CreateIndexSet(stem, prefix, p_idx):
    p_m_idx = copy.deepcopy(p_idx)
    for record in p_m_idx.Records:
        if prefix is None:
            start_pos = 0
        else:
            start_pos = record.pos
        for i in range(start_pos+1, record[-1]):
            if stem in p_m_idx.Records:
                IndexRecord.Interval = [stem.Start, stem.End]
                p_m_idx.Records.append(IndexRecord[start_pos + i], IndexRecord.Interval, start_pos)
    return p_m_idx


# MDB is the list of client sequences
def CreateFirstIndexSet(stem, MDB):
    idx = IndexSet(stem.State, [])
    for singleState in range(0, len(MDB)):
        if MDB.iloc[singleState].State == stem.State:
            ref = MDB.iloc[singleState].ClientID
            intv = [MDB.iloc[singleState].Start, MDB.iloc[singleState].End]
            new_rec = IndexRecord(MDB.iloc[singleState].Start, intv, ref)
            idx.Records.append(new_rec)
    for i in idx.Records:
        print(i)
    return idx
