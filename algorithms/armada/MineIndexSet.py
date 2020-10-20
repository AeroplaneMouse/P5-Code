# from CreateIndexSet import CreateIndexSet
# from CreatePattern import CreatePattern
from algorithms.armada import Storage
import findSupport


# Computes new stems
# Assumes that cs only contains states that is above minSup
def ComputePotentialStems(indexSet, frequentStates, minSup):
    # TODO
    # Add check for record state == potential stem state
    
    # Key points---
    # - Any state in the refrenced cs where state pos > record.pos == potential stem
    # - Increment support count for specific state

    # Dictionary of potential stems
    pStems = {}

    for record in indexSet.Records:
        # Retrieve cs from reference
        cs = Storage.MDB[record.Ref]

        # Increment support count for every state in cs
        # after pos in indexSet record
        for csIndex in range(record.Pos, len(cs)):
            singleCS = cs.iloc[csIndex]

            # Insert state into stem if not there
            if singleCS.State not in pStems:
                pStems[singleCS.State] = []

            # Insert clientID if not there
            clientID = singleCS.ClientID
            if clientID not in pStems[singleCS.State]:
                pStems[singleCS.State].append(clientID)

    # Print pStems content
    # for key in pStems.keys():
    #     print('{} | {}'.format(key, pStems[key]))

    print('Potential stems:')
    # Add frequent states to stems
    stems = []
    clients = cs[:1].at[0, 'ClientID'] + 1
    for s in pStems:
        sup = len(pStems[s]) / clients
        print('{} | {:.2f}'.format(s, sup))
        if sup >= minSup:
            stems.append(s)  # Maybe do something to get FState. IDK might be useful 

    return stems


def MineIndexSet(pattern, indexSet, frequentStates, cs):
    stems = ComputePotentialStems(indexSet, frequentStates)

    # rSet = []
    # prefix = None  # Mock
    # for s in stems:
    #     p = CreatePattern(prefix, s)
    #     iSet = CreateIndexSet(s, p, rSet)
    #     MineIndexSet(p, iSet)
