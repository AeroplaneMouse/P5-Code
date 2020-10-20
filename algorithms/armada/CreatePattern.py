import numpy as np
# from models.TPattern import TPattern
# from models.FState import FState
from algorithms.armada.FindRelation import FindRelation


def CreatePattern(prefix, stem):

    if prefix is None:
        temp = np.ndarray((2, 2), dtype='object')
        temp[0][1] = stem
        temp[1][0] = stem
        temp[1][1] = '='
        return temp

    elif prefix is np.ndarray:
        dimension = np.shape(prefix)[0]
        temp = np.reshape(prefix, (dimension+1, dimension+1))

        for i in range(dimension):
            temp[i+1][dimension] = FindRelation(temp[0][i+1], stem)
            temp[dimension][i+1] = '*'

        temp[0][dimension] = stem
        temp[dimension][0] = stem
        temp[dimension][dimension] = '='
        return temp

    else:
        return None
