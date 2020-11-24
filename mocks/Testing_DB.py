from tpmmodels.Endpoint import Endpoint
from tpmmodels.DB import DB

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

Seq_1 = [a_s, b_s, b_f, a_f, c_s, c_f]
Seq_2 = [a_s, b_s, b_f, a_f, c_s, c_f]
Seq_3 = [a_s, b_s, b_f, a_f, c_s, c_f]
Seq_4 = [a_s, b_s, b_f, a_f, c_s, c_f]
Seq_5 = [a_s, b_s, b_f, a_f, c_s, c_f]
Seq_6 = [a_s, b_s, b_f, a_f, c_s, c_f]
Seq_7 = [a_s, b_s, b_f, a_f, c_s, c_f]
Seq_8 = [a_s, b_s, b_f, a_f, c_s, c_f]

EP_list = [Seq_1, Seq_2, Seq_3, Seq_4, Seq_5, Seq_6, Seq_7, Seq_8]

db = DB([a_s])
db.ES = EP_list