from tpmmodels.DB import DB
from tpmmodels.Projected_cs import Projected_cs
import copy
import pdb, traceback, sys


#Calls the auxillary functions responsible for creating the pruned database and the a' database
def db_construct(db_a, p, temp):

    db_a_p = create_db_a_p(db_a, p, temp)

    prune(db_a_p, temp)

    return db_a_p


#Used to create the a' database, using the projected database and a prefix
def create_db_a_p(db_a, p, temp):
    db_a_p = DB(db_a.Pattern + [p])

    if not p.In_paren:
        for cs in db_a.ES:
            prefix = cs.Prefix_instance
            paren_num = prefix[-1].Parenthesis if len(prefix) > 0 else 0
            stop_pos = find_stop_pos(cs.Ep_list, db_a.Prfx_s_ep)
            i = 0
            while i < stop_pos and cs.Ep_list[i].Parenthesis == paren_num:
                i = i + 1
            for ep in cs.Ep_list[i:stop_pos+1]:
                i = i + 1
                if ep == p:
                    new_eps = cs.Ep_list[i:]
                    if len(new_eps) > 0:
                        ##debugging
                        #ep_new = copy.deepcopy(ep)
                        #ep_new.Stop_pos = stop_pos
                        #ep_new.Ep_list = copy.copy(new_eps)
                        ##
                        p_cs = Projected_cs(copy.copy(cs.Prefix_instance) + [ep])
                        p_cs.Ep_list = new_eps
                        p_cs.cs_id = cs.cs_id
                        db_a_p.ES.append(p_cs)
                    break
    else:
        for cs in db_a.ES:
            paren_num = cs.Prefix_instance[-1].Parenthesis
            stop_pos = find_stop_pos(cs.Ep_list, db_a.Prfx_s_ep)
            i = 0
            while i < stop_pos and cs.Ep_list[i].Parenthesis == paren_num:
                if cs.Ep_list[i] == p:
                    ep_new = cs.Ep_list[i]
                    del cs.Ep_list[i]
                    new_eps = cs.Ep_list
                    if len(new_eps) > 0:
                        ##debugging
                        #ep_new.Stop_pos = stop_pos
                        #ep_new.Ep_list = copy.copy(new_eps)
                        ##
                        p_cs = Projected_cs(copy.copy(cs.Prefix_instance) + [ep_new])
                        p_cs.Ep_list = new_eps
                        p_cs.cs_id = cs.cs_id
                        db_a_p.ES.append(p_cs)
                    break
                i = i + 1

    return db_a_p


#prunes a ENDPOINT SEQUENCE (cs) using a list of starting endpoints, to check that finishing endpoints have
#a corresponding starting endpoint
def prune(db, temp):
    for cs in db.ES:
        pruned_eps = []
        #for i in reversed(range(len(cs.Ep_list))):
        for i in range(len(cs.Ep_list)):
            if not cs.Ep_list[i].IsStart:
                f_ep = cs.Ep_list[i]
                for ep in reversed(db.Prfx_s_ep + cs.Ep_list[:i]):
                    if ep.Label == f_ep.Label and ep.IsStart and not ep.Prune:
                        ep.Prune = True
                        f_ep.Prune = False
                        break
                else:
                    f_ep.Prune = True

        for ep in cs.Ep_list:
            if ep.IsStart or not ep.Prune:
                pruned_eps.append(ep)
            ep.Prune = False

        for ep in db.Prfx_s_ep:
            ep.Prune = False


        cs.Ep_list = pruned_eps
        


#Just compares the given endpoint (ep) to a list of starting endpoint, to make sure that the endpoint has
#a corresponding endpoint with the same label, in the list of starting endpoints


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
