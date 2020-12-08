import copy


def remove_corresponding_eps(prfx):
    temp = copy.deepcopy(prfx)

    i = 0
    j = len(prfx)-1
    while i < j:
        if prfx[i].IsStart:
            for k in range(i, j):
                if prfx[i].Label == prfx[j].Label and not prfx[j].IsStart:
                    del temp[j]
                    j = j - 1
                    break
        i = i + 1
        
    return temp