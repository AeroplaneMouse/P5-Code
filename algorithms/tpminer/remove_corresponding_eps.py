

def remove_corresponding_eps(prfx):
    s_ep = list(filter(lambda x : x.IsStart, prfx))
    f_ep = list(filter(lambda x : not x.IsStart, prfx))

    for f in f_ep:
        i = 0
        while f.Label != s_ep[i].Label:
            i += 1
        del s_ep[i]

    return s_ep