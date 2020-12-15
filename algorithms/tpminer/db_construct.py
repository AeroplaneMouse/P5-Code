from tpmmodels.DB import DB
from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
from tpmmodels.Projected_cs import Projected_cs
import copy

#Calls the auxillary functions responsible for creating the pruned database and the a' database
def db_construct(db_a, p):

    db_a_p = create_db_a_p(db_a, p)
    pruned_db = DB(db_a.Pattern + [p])

    for cs in db_a_p.ES:
        new_cs = prune(cs, db_a_p.Prfx_s_ep)
        if len(new_cs.Ep_list) > 0:
            pruned_db.ES.append(new_cs)

    return pruned_db, db_a_p

#Used to create the a' database, using the projected database and a prefix
def create_db_a_p(db_a, p):
    db_a_p = DB(db_a.Pattern + [p])

    if not p.In_paren:
        for cs in db_a.ES:
            stop_pos = find_stop_pos(cs.Ep_list, db_a.Prfx_s_ep)
            i = 0
            for ep in cs.Ep_list[:stop_pos+1]:
                i = i + 1
                if ep == p:
                    new_eps = cs.Ep_list[i:]
                    if len(new_eps) > 0:
                            p_cs = Projected_cs(copy.copy(cs.Prefix_instance) + [ep])
                            p_cs.Ep_list = new_eps
                            p_cs.cs_id = cs.cs_id
                            db_a_p.ES.append(p_cs)
                    break
    else:
        for cs in db_a.ES:
            stop_pos = find_stop_pos(cs.Ep_list, db_a.Prfx_s_ep)
            paren_num = cs.Prefix_instance[-1].Parenthesis
            i = 0
            while i < stop_pos and cs.Ep_list[i].Parenthesis == paren_num:
                if cs.Ep_list[i] == p:
                    new_eps = cs.Ep_list[i+1:]
                    if len(new_eps) > 0:
                            p_cs = Projected_cs(copy.copy(cs.Prefix_instance) + [cs.Ep_list[i]])
                            p_cs.Ep_list = new_eps
                            p_cs.cs_id = cs.cs_id
                            db_a_p.ES.append(p_cs)
                    break
                i = i + 1
    return db_a_p

#prunes a ENDPOINT SEQUENCE (cs) using a list of starting endpoints, to check that finishing endpoints have
#a corresponding starting endpoint
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


#Just compares the given endpoint (ep) to a list of starting endpoint, to make sure that the endpoint has
#a corresponding endpoint with the same label, in the list of starting endpoints
def has_corresponding_ep(ep, s_ep):
    for s in s_ep:
        if ep.Label == s.Label:
            return True
    else:
        return False

#Finds the stop position for a given prefix, in a endpoint sequence (eps)
def find_stop_pos(eps, prfx_s):
    if len(prfx_s) > 0:
        for ep in eps:
            if not ep.IsStart:
                if is_in_prfx(ep, prfx_s):
                    return eps.index(ep)
    else:
        return len(eps)-1

#Used in above function to ensure that the given endpoint has the same label as the one in the prefix
def is_in_prfx(ep, prfx_s):
    for p in prfx_s:
        if ep.Label == p.Label:
            return True
    return False

