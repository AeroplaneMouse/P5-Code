import numpy as np
from algorithms.armada.FindRelation import FindRelation


def CreatePattern(prefix, stem):
    #if there is no prefix pattern, create one-pattern from stem
    if prefix is None:
        temp = np.ndarray((2, 2), dtype='object')
        temp[0][1] = stem
        temp[1][0] = stem
        temp[1][1] = '='
        return temp
    
    #append prefix
    else:

        dimension = np.shape(prefix)[0]
        temp = np.concatenate((prefix, np.zeros((1, dimension), dtype='object')))
        temp = np.concatenate((temp, np.zeros((dimension+1, 1), dtype='object')), axis=1)

        #compute relations for each cell
        for i in range(dimension-1):
            temp[i+1][dimension] = FindRelation(temp[0][i+1], stem)
            temp[dimension][i+1] = '*'

        temp[0][dimension] = stem
        temp[dimension][0] = stem
        temp[dimension][dimension] = '='
        return temp
