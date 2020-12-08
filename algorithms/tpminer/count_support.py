from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
from tpmmodels.Ep_sup import Ep_sup
from tpmmodels.Endpoint import Endpoint
from tpmmodels.Projected_cs import Projected_cs

#def count_support(db_a, min_sup, lone_eps):
def count_support(db_a, min_sup):
    suppList = []
    FE = set()

    lone_eps = remove_corresponding_eps(db_a.Pattern)

    for cs in db_a.ES:
        if len(cs.Ep_list) > 0:
            j = find_stop_pos(cs.Ep_list, lone_eps, cs.cs_id)
            acc_sup(cs.Ep_list[:j], suppList, cs.Prefix_instance[-1].Parenthesis)

    cs_n = len(db_a.ES)
    for ep in suppList:
        if ep.Support / cs_n >= min_sup:
            FE.add(Endpoint(ep.Label, ep.IsStart, 0))
        #if ep.In_paren_supp / cs_n >= min_sup:
            #FE.add(Endpoint(ep.Label, ep.IsStart, 1))


    return FE

def find_stop_pos(ep_list, prfx_s_ep, id):
    cs_len = len(ep_list)
    if len(prfx_s_ep) > 0:
        i = 0
        while not is_stop_ep(ep_list[i], prfx_s_ep):
            i += 1
        p = ep_list[i].Parenthesis
        #if p > 0:
        if False:
            while i < cs_len - 1 and ep_list[i + 1].Parenthesis == p:
                i += 1
        return i + 1
    else:
        return cs_len

def is_stop_ep(ep, prfx_s_ep):
    if not ep.IsStart:
        for s_ep in prfx_s_ep:
            if ep.Label == s_ep.Label:
                return True
        return False
    else:
        return False

def acc_sup(cs, suppList, paren_num):
    i = 0

    #in parenthesis support
    if False:
    #if paren_num > 0:
        while i < len(cs):
            if cs[i].Parenthesis == paren_num:
                is_in_list = False
                for j in range(len(suppList)):
                    if cs[i].Label == suppList[j].Label and cs[i].IsStart == suppList[j].IsStart:
                        if not suppList[j].Has_been_counted:
                            suppList[j].In_paren_supp += 1
                            suppList[j].Has_been_counted = True
                        is_in_list = True

                if not is_in_list:
                    suppList.append(Ep_sup(cs[i].Label, cs[i].IsStart, 0, 1))
                i += 1
            else:
                break
    
    #not in parenthesis support
    while i < len(cs):
        is_in_list = False
        for j in range(len(suppList)):
            #if not cs[i].Prune and cs[i].Label == suppList[j].Label and cs[i].IsStart == suppList[j].IsStart:
            if cs[i].Label == suppList[j].Label and cs[i].IsStart == suppList[j].IsStart:
                if not suppList[j].Has_been_counted:
                    suppList[j].Support += 1
                    suppList[j].Has_been_counted = True
                is_in_list = True
        if not is_in_list:
            suppList.append(Ep_sup(cs[i].Label, cs[i].IsStart, 1, 0))
        i += 1

    for e in suppList:
        e.Has_been_counted = False
