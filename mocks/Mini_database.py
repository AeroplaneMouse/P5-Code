from tpmmodels.Endpoint import Endpoint
import copy

cs = []

a_p = Endpoint('A', False, 0)

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

db = []
db.append(cs)
db.append(cs2)
db.append(cs3)
db.append(cs4)
db.append(cs5)

