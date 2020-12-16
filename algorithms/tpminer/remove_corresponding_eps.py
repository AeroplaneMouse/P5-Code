import copy


def remove_corresponding_eps(prfx):
    s_ep = list(filter(lambda x: x.IsStart, prfx))
    f_ep = list(filter(lambda x: not x.IsStart, prfx))

    for f in f_ep:
        i = 0
        while s_ep[i].Label != f.Label:
            i = i + 1
        del s_ep[i]

    return s_ep