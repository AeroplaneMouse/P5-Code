import numpy as np
from models.TPattern import TPattern
from models.FState import FState
from algorithms.armada.FindRelation import FindRelation

def CreatePattern(prefix, stem):

    matrix = prefix.Matrix
    dimension = np.shape(matrix)[0]

    newMatrix = np.reshape(matrix, (dimension + 1, dimension + 1))

    newMatrix[0][dimension] = stem.State

    for i in range(dimension):
        newMatrix[i+1][dimension] = FindRelation(newMatrix[0][i+1], stem)

    newMatrix[dimension][dimension] = '='

    return newMatrix
