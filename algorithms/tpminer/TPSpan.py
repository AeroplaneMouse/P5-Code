from algorithms.tpminer.count_support import count_support
from algorithms.tpminer.db_construct import db_construct
from algorithms.tpminer.point_pruning import point_pruning

def TPSpan(a, db_a, min_occ, TP, temp):
    FE = count_support(db_a, min_occ, temp)
    FE = point_pruning(FE, a, db_a.Prfx_s_ep)

    for s in FE:
        a_p = a + [s]

        db_a_p = db_construct(db_a, s, temp)

        if len(db_a_p.Prfx_s_ep) == 0:	
            TP.add(tuple(filter(lambda x: (x.Parenthesis, x.IsStart, x.Label), a_p)))
            if len(TP) % 10000 == 0: print(len(TP))
    
        TPSpan(a_p, db_a_p, min_occ, TP, temp)

