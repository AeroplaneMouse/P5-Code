import copy


def remove_corresponding_eps(prfx):
    s_ep = set(filter(lambda x: x.IsStart, prfx))
    f_ep = set(filter(lambda x: not x.IsStart, prfx))

    temp = list(copy.copy(s_ep))

    for f in f_ep:
        i = 0
        while temp[i].Label != f.Label:
            i = i + 1
        del temp[i]

    return temp