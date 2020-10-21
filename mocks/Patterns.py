import numpy as np
from mocks import FStates


A = np.ndarray((2, 2), dtype='object')
A[0][1] = FStates.D
A[1][0] = FStates.D
A[1][1] = '='


B = np.ndarray((2, 2), dtype='object')
B[0][1] = FStates.E
B[1][0] = FStates.E
B[1][1] = '='


All = [A, B]
