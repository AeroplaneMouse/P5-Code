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

C = np.ndarray((4, 4), dtype='object')
C[0][1] = FStates.F
C[0][2] = FStates.G
C[0][3] = FStates.H
C[1][0] = FStates.F
C[2][0] = FStates.G
C[3][0] = FStates.H
C[1][1] = '='
C[2][2] = '='
C[3][3] = '='
C[1][2] = 'S'
C[1][3] = 'O'
C[2][3] = 'O'

D = np.ndarray((2, 2), dtype='object')
D[0][1] = FStates.F
D[1][0] = FStates.F
D[1][1] = '='

E = np.ndarray((3, 3), dtype='object')
E[0][1] = FStates.F
E[0][2] = FStates.G
E[1][0] = FStates.F
E[2][0] = FStates.G
E[1][1] = '='
E[2][2] = '='
E[1][2] = 'S'


All = [A, B, C]
