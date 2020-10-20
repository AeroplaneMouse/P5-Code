import numpy as np
# from models.TPattern import TPattern
# from models.FState import FState
from algorithms.armada.FindRelation import FindRelation


def CreatePattern(prefix, stem):

    temp = prefix
    dimension = np.shape(temp)[0]

    if(dimension > 1):
        temp = np.reshape(temp, (dimension + 1, dimension + 1))
        for i in range(dimension):
            temp[i+1][dimension] = FindRelation(temp[0][i+1], stem)
            temp[dimension][i+1] = '*'

    else:
        temp = np.ndarray((2, 2), dtype='object')

    temp[0][dimension] = stem
    temp[dimension][0] = stem
    temp[dimension][dimension] = '='

    return newMatrix
