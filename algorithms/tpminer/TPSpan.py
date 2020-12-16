from algorithms.tpminer.count_support import count_support
from algorithms.tpminer.db_construct import db_construct
from algorithms.tpminer.point_pruning import point_pruning
from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
import copy

def TPSpan(a, db_a, min_occ, TP, db_pruned, temp):
    FE = count_support(db_pruned, min_occ, temp)
    FE = point_pruning(FE, a, db_a.Prfx_s_ep)

    FE = set(filter(lambda x : eligible(a, x), FE))
    for s in FE:
        a_p = a + [s]

        db_pruned, db_a_p = db_construct(db_a, s, temp)

        if len(db_a_p.Prfx_s_ep) == 0:	
            TP.add(tuple(a_p))
    
        TPSpan(a_p, db_a_p, min_occ, TP, db_pruned, temp)


def eligible(a, x):
    if x.IsStart:
        for ep in a:
            if ep.Label == x.Label:
                return False
        else:
            return True
    else:
        return True

