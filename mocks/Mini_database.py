from tpmmodels.Endpoint import Endpoint

cs = []

cs.append(Endpoint('A', True, 0))
cs.append(Endpoint('A', False, 0))

#To be postfix pruned
cs.append(Endpoint('B', False, 0))

cs.append(Endpoint('C', True, 0))
cs.append(Endpoint('C', False, 0))
cs.append(Endpoint('D', True, 0))
cs.append(Endpoint('D', False, 0))