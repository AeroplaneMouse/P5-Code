from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
from tpmmodels.Ep_sup import Ep_sup
from tpmmodels.Endpoint import Endpoint
from tpmmodels.Projected_cs import Projected_cs

def count_support(db_a, min_occ):
    FE = set()
    support_list = []

    for eps in db_a.ES:
        stop_pos = find_stop_pos(eps.Ep_list, db_a.Prfx_s_ep)
        if stop_pos == None:
            stop_pos = len(eps.Ep_list)-1
        support_list = acc_sup(eps.Ep_list, support_list, stop_pos)

    for ep in support_list:
        if ep.Support >= min_occ:
            FE.add(ep)
    return FE


def find_stop_pos(eps, prfx_s):
    pos = len(eps)-1
    if len(prfx_s) > 0:
        for ep in eps:
            if not ep.IsStart:
                if is_in_prfx(ep, prfx_s):
                    pos = eps.index(ep)
    return pos


def is_in_prfx(ep, prfx_s):
    for p in prfx_s:
        if ep.Label == p.Label:
            return True
    return False


# Accumulated support
def acc_sup(eps, support_list, stop_pos):
    if len(eps) > 0:
        for ep in eps[:stop_pos+1]:
            for s in support_list:
                if s == ep:
                    if not s.Counted:
                        s.Support = s.Support + 1
                        s.Counted = True
                    break
            else:
                s_new = Endpoint(ep.Label, ep.IsStart, 0)
                s_new.Support = s_new.Support + 1
                s_new.Counted = True
                support_list.append(s_new)

        for s in support_list:
            s.Counted = False

    return support_list