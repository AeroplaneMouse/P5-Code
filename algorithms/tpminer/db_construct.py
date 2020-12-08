from tpmmodels.DB import DB
from algorithms.tpminer.remove_corresponding_eps import remove_corresponding_eps
from tpmmodels.Projected_cs import Projected_cs

#def db_construct(db_a, a_p, lone_eps):
def db_construct(db_a, a_p):
    temp_seq = DB(a_p)

    lone_eps = remove_corresponding_eps(a_p)

    #in_paren = False
    #if len(a_p) > 1:
        #if a_p[-2].Parenthesis > 0 and a_p[-2].Parenthesis == a_p[-1].Parenthesis:
            #in_paren = True

    #db_a_p = create_db_paren(db_a, a_p) if in_paren else create_db(db_a, a_p)

    db_a_p = create_db(db_a, a_p)

    for cs in db_a_p.ES:
        new_cs = postfix_prune(cs, a_p, lone_eps)
        temp_seq.ES.append(new_cs)

    return temp_seq, db_a_p

def create_db(db_a, a_p):
    db_a_p = DB(a_p)
    a_last = a_p[-1]

    for cs in db_a.ES:
        i = 0
        for ep in cs.Ep_list:
            i += 1
            if ep.Label == a_last.Label and ep.IsStart == a_last.IsStart:
                new_cs = Projected_cs(cs.Prefix_instance + [ep])
                new_cs.cs_id = cs.cs_id
                new_cs.Ep_list.extend(cs.Ep_list[i:])
                db_a_p.ES.append(new_cs)
                break
    return db_a_p

def create_db_paren(db_a, a_p):
    db_a_p = DB(a_p)
    a_last = a_p[-1]

    for cs in db_a.ES:
        paren_num = cs.Prefix_instance[-1].Parenthesis
        if paren_num > 0:
            cs_len = len(cs.Ep_list)
            i = 0
            for ep in cs.Ep_list:
                if ep.Parenthesis == paren_num:
                    i += 1
                    if ep.Label == a_last.Label and ep.IsStart == a_last.IsStart:
                        new_cs = Projected_cs(cs.Prefix_instance + [ep])
                        new_cs.Ep_list.extend(cs.Ep_list[i:])
                        db_a_p.ES.append(new_cs)
                        break
                else:
                    break

    return db_a_p

def postfix_prune(cs, a_p, s_ep):
    for ep in cs.Ep_list:
        if ep.IsStart == False:
            ep.Prune = True
            for s in s_ep:
                if ep.Label == s.Label:
                    ep.Prune = False
                    break
    new_cs = Projected_cs(cs.Prefix_instance)
    new_cs.Ep_list = prune(cs.Ep_list)
    return new_cs

def prune(cs):
    new_cs = []
    for ep in cs:
        if not ep.Prune:
            new_cs.append(ep)

    return new_cs
