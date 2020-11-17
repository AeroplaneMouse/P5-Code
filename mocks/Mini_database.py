from tpmmodels.Endpoint import Endpoint
from tpmmodels.DB import DB
import copy


prfx = [Endpoint('B', True, 0)]
a_p = copy.deepcopy(prfx)
a_p.append(Endpoint('A', False, 0))

cs = []

cs.append(Endpoint('A', True, 0))
cs.append(Endpoint('A', False, 0))

#To be postfix pruned
cs.append(Endpoint('B', False, 0))

cs.append(Endpoint('C', True, 0))
cs.append(Endpoint('C', False, 0))
cs.append(Endpoint('D', True, 0))
cs.append(Endpoint('D', False, 0))

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

