from models.IndexSet import IndexSet
from models.IndexRecord import IndexRecord
import copy as copy
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada import Storage
from models.Interval import Interval

# range set is an index set.
def CreateIndexSet(stem, prefix, p_idx):
    p_m_idx = copy.deepcopy(p_idx)
    for record in p_m_idx.Records:
        start_pos = record.pos
        for i in range(start_pos+1, record[-1]):
            if stem in p_m_idx.Records:
                

                p_m_idx
    return p_m_idx


# MDB is the list of client sequences
# visited_states is used to keep check of frequent states that already have an index set
def CreateFirstIndexSet(stem, visited_states):
    idx = IndexSet(stem.State, [])
    if stem.State not in visited_states:
        visited_states.append(stem.State)
        for cs in Storage.MDB:
            for singleState in range(0,len(cs)):
                if cs.iloc[singleState].State == stem.State:
                    
                    ref = cs.at[0, 'ClientID']
                    intv = [Interval(cs.iloc[singleState].Start, cs.iloc[singleState].End)]
                    pos = singleState

                    new_rec = IndexRecord(pos, intv, ref)

                    idx.Records.append(new_rec)
                    break
            continue
        return idx