import numpy as np
from models.TPattern import TPattern

def CreatePattern(prefix, stem):

	dimension = np.shape(prefix)[0]

    newPattern = np.reshape(prefix, (dimension + 1, dimension + 1))

    return TPattern.matrix
