from tpmmodels.Endpoint import Endpoint
from tpmmodels.DB import DB
import copy

a_s = Endpoint('A', True, 0)
a_f = Endpoint('A', False, 0)
b_s = Endpoint('B', True, 0)
b_f = Endpoint('B', False, 0)
c_s = Endpoint('C', True, 0)
c_f = Endpoint('C', False, 0)
d_s = Endpoint('D', True, 0)
d_f = Endpoint('D', False, 0)
e_s = Endpoint('E', True, 0)
e_f = Endpoint('E', False, 0)
f_s = Endpoint('F', True, 0)
f_f = Endpoint('F', False, 0)
g_s = Endpoint('G', True, 0)
g_f = Endpoint('G', False, 0)


#with parenthesis
a_s_1 = Endpoint('A', True, 1)
a_f_1 = Endpoint('A', False, 1)
b_s_1 = Endpoint('B', True, 1)
b_f_1 = Endpoint('B', False, 1)
c_s_1 = Endpoint('C', True, 1)
c_f_1 = Endpoint('C', False, 1)