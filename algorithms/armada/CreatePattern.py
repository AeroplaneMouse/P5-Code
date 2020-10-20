import numpy as np
from models.TPattern import TPattern
from models.FState import FState
from algorithms.armada.FindRelation import FindRelation

def CreatePattern(prefix, stem):

    matrix = prefix.Matrix
    dimension = np.shape(matrix)[0]


    if(dimension > 1):
        newMatrix = np.reshape(matrix, (dimension + 1, dimension + 1))
        for i in range(dimension):
            newMatrix[i+1][dimension] = FindRelation(newMatrix[0][i+1], stem)
            newMatrix[dimension][i+1] = '*'

    else:
        newMatrix = np.ndarray((2, 2), dtype='object')

    newMatrix[0][dimension] = stem.State
    newMatrix[dimension][0] = stem.State
    newMatrix[dimension][dimension] = '='

    return newMatrix
