import numpy as np
from models.TPattern import TPattern

def CreatePattern(prefix, FState):



    for i in range(np.shape(FState)[0]):

        if (FState.end < prefix.start):
            FState.state = "Before"
        elif (FState.end > prefix.start && FState.end < prefix.end):
            FState.state = "Overlaps"
        elif (FState.end == prefix.start):
            FState.state = "Begins"
        elif (FState.end == prefix.end):
            FState.state = "Ends"
        elif (FState.start < prefix.start && FState.end > prefix.end):
            FState.state = "Contains"


    np.pad(prefix, ((0, 1), (0, 1)), mode='constant', constant_values=0)



    array_size = prefix * FState.state
    TPattern.matrix = np.arrange(array_size).reshape(prefix, FState.state)

    return TPattern.matrix
