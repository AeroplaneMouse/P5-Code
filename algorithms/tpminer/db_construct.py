from tpmmodels.DB import DB
from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
from tpmmodels.Projected_cs import Projected_cs
import copy

def db_construct(db_a, p):

    db_a_p = create_db_a_p(db_a, p)
    pruned_db = DB(db_a.Pattern + [p])

    for cs in db_a_p.ES:
        new_cs = prune(cs, db_a_p.Prfx_s_ep)
        if len(new_cs.Ep_list) > 0:
            pruned_db.ES.append(new_cs)

    return pruned_db, db_a_p


def create_db_a_p(db_a, p):
    db_a_p = DB(db_a.Pattern + [p])

    for cs in db_a.ES:
        for ep in cs.Ep_list:
            if ep == p:
                i = cs.Ep_list.index(ep)
                if i < len(cs.Ep_list) - 1:
                    p_cs = Projected_cs(copy.deepcopy(cs.Prefix_instance) + [ep])
                    p_cs.cs_id = cs.cs_id
                    p_cs.Ep_list = cs.Ep_list[i+1:]
                    db_a_p.ES.append(p_cs)
                    break
    return db_a_p

def prune(cs, s_ep):
    pruned_cs = Projected_cs(copy.deepcopy(cs.Prefix_instance))
    pruned_cs.cs_id = cs.cs_id

    new_eps = []
    for ep in cs.Ep_list:
        if ep.IsStart:
            new_eps.append(ep)
        elif not ep.IsStart:
            if has_corresponding_ep(ep, s_ep):
                new_eps.append(ep)

    pruned_cs.Ep_list = new_eps

    return pruned_cs



def has_corresponding_ep(ep, s_ep):
    for s in s_ep:
        if ep.Label == s.Label:
            return True
    else:
        return False

