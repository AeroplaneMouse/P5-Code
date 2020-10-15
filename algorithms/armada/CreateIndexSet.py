from models.IndexSet import IndexSet
from models.IndexRecord import IndexRecord
import copy as copy

# range set is an index set.
def CreateIndexSet(stem, prefix, p_idx):
    p_m_idx = copy.deepcopy(p_idx)
    for cs in p_m_idx.Records:
        if prefix == None:
            start_pos = 0
        else:
            start_pos = cs.pos
        for i in range(start_pos+1, cs[-1]):
            if stem in p_m_idx.Records:
                p_m_idx.Records.append(IndexRecord[start_pos + i], IndexRecord.Interval, start_pos)
    return p_m_idx