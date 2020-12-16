from tpmmodels.Endpoint import Endpoint

#Calls the auxillary functions responsible for creating the Frequent Endpoint list
def count_support(db_a, min_occ, temp):
    FE = set()
    support_list = []

    for eps in db_a.ES:
        stop_pos = find_stop_pos(eps.Ep_list, db_a.Prfx_s_ep)
        support_list = acc_sup(eps, support_list, stop_pos, temp)

    for ep in support_list:
        if ep.Support >= min_occ:
            FE.add(ep)
    return FE

#uses a list of endpoint sequences and the starting prefix, to find the stop position
def find_stop_pos(eps, prfx_s):
    if len(prfx_s) > 0:
        for ep in eps:
            if not ep.IsStart:
                if is_in_prfx(ep, prfx_s):
                    return eps.index(ep)
    else:
        return len(eps)-1

#Used to check that a given endpoint is in the prefix, by comparing labels
def is_in_prfx(ep, prfx_s):
    for p in prfx_s:
        if ep.Label == p.Label:
            return True
    return False


# Accumulated support
def acc_sup(eps, support_list, stop_pos, temp):
    paren_num = eps.Prefix_instance[-1].Parenthesis
    i = 0
    if len(eps.Ep_list) > 0:
        while i <= stop_pos and eps.Ep_list[i].Parenthesis == paren_num:
            for s in support_list:
                if s == eps.Ep_list[i] and s.In_paren:
                    if not s.Counted:
                        s.Support = s.Support + 1
                        s.Counted = True
                    break
            else:
                s_new = Endpoint(eps.Ep_list[i].Label, eps.Ep_list[i].IsStart, 0)
                s_new.In_paren = True
                s_new.Support = s_new.Support + 1
                s_new.Counted = True
                support_list.append(s_new)

            i = i + 1

        for ep in eps.Ep_list[i:stop_pos+1]:
            for s in support_list:
                if s == ep and not s.In_paren:
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