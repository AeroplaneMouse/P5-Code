from algorithms.tpminer.count_support import count_support
from algorithms.tpminer.db_construct import db_construct
from algorithms.tpminer.point_pruning import point_pruning
from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
import copy

def TPSpan(a, db_a, min_sup, TP):
    FE = count_support(db_a, min_sup)
    for s in FE:
        print(s)

    FE = point_pruning(FE, a)
    for s in FE:
        print("   " + str(s))
    print()

    for s in FE:
        a_prime = a + [s]
        print(a_prime)
        if len(remove_corresponding_eps(a_prime)) == 0:	
            TP.add(tuple(a_prime))

        for cs in db_a.ES:
            print(cs.Ep_list)

        db_a_prime = db_construct(db_a, a_prime)

        for cs in db_a_prime.ES:
            print(cs.Ep_list)

        TPSpan(a_prime, db_a_prime, min_sup, TP)
