from tpmmodels.Endpoint import Endpoint
from tpmmodels.DB import DB
import copy

a_start = Endpoint('A', True, 0)
a_finish = Endpoint('A', False, 0)
b_start = Endpoint('B', True, 0)
b_finish = Endpoint('B', False, 0)
c_start = Endpoint('C', True, 0)
c_finish = Endpoint('C', False, 0)
d_start = Endpoint('D', True, 0)
d_finish = Endpoint('D', False, 0)

prfx = [a_start]
prfx2 = [d_start]
prfx3 = [b_start, d_start]

a_p = copy.deepcopy(prfx)

cs = []

cs.append(a_finish)
cs.append(b_finish)
cs.append(c_start)
cs.append(c_finish)
cs.append(d_start)
cs.append(d_finish)

cs2 = copy.deepcopy(cs)
cs3 = copy.deepcopy(cs)
cs4 = copy.deepcopy(cs)
cs5 = copy.deepcopy(cs)

db = DB(prfx)
db.ES.append(cs)
db.ES.append(cs2)
db.ES.append(cs3)
db.ES.append(cs4)
db.ES.append(cs5)

cs2 = [a_start, b_start, b_finish, c_start, a_finish, d_start, d_finish, c_finish]

