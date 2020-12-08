from algorithms.tpminer.count_support import count_support
from algorithms.tpminer.db_construct import db_construct
from algorithms.tpminer.point_pruning import point_pruning
from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
import copy

#def TPSpan(a, db_a, min_sup, TP, lone_eps):
#def TPSpan(a, db_a, min_sup, TP):
def TPSpan(a, db_a, min_sup, TP, db_pruned):
    #FE = count_support(db_a, min_sup, lone_eps)
    #FE = point_pruning(FE, a, lone_eps)
    FE = count_support(db_pruned, min_sup)
    FE = point_pruning(FE, a)

    for s in set(filter(lambda x : not in_pattern(a, x), FE)):
    #for s in FE:
        a_prime = a + [s]

        #lone_eps = append_lone_eps(lone_eps, s)
        lone_eps = remove_corresponding_eps(a_prime)
        if len(lone_eps) == 0:	
            TP.add(tuple(a_prime))

        #db_a_prime = db_construct(db_a, a_prime, lone_eps)
        db_pruned, db_a_prime = db_construct(db_a, a_prime)

        #TPSpan(a_prime, db_a_prime, min_sup, TP, lone_eps)
        TPSpan(a_prime, db_a_prime, min_sup, TP, db_pruned)


def in_pattern(a, x):
    if x.IsStart:
        for ep in a:
            if ep == x:
                return True
        return False
    else:
        return False

def append_lone_eps(lone_eps, s):
    if s.IsStart:
        lone_eps.append(s)
    elif not s.IsStart:
        for ep in lone_eps:
            if ep.Label == s.Label and ep.IsStart:
                lone_eps.remove(ep)
                break
    return lone_eps
