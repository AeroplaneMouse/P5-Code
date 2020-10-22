# from CreateIndexSet import CreateIndexSet
# from CreatePattern import CreatePattern
from algorithms.armada import Storage
from preprocessors import Support
from models.PState import PState
from models.FState import FState


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
        for csIndex in range(record.Pos + 1, len(cs)):
            csRecord = cs.iloc[csIndex]

            # Insert state into stem if not there
            if csRecord.State not in pStems:
                pStems[csRecord.State] = PState(csIndex)

            # Insert clientID if not there
            clientID = csRecord.ClientID
            if clientID not in pStems[csRecord.State].AppearsIn:
                pStems[csRecord.State].AppearsIn.append(clientID)

    # Print pStems content
    # for key in pStems.keys():
    #     print('{} | {}'.format(key, pStems[key]))

    print('Potential stems:')
    # Add frequent states to stems
    stems = []
    clients = cs[:1].at[0, 'ClientID'] + 1
    for s in pStems:
        support = len(pStems[s].AppearsIn) / clients
        print('{} | {}  {:.2f}'.format(s, pStems[s].Pos, support))
        if support >= minSup:
            # Create FState
            state = FState(s, None, None)
            stems.append(state)

    return stems


def MineIndexSet(pattern, indexSet, frequentStates, cs):
    stems = ComputePotentialStems(indexSet, frequentStates)

    # rSet = []
    # prefix = None  # Mock
    for s in stems:
        p = CreatePattern(prefix, s)
        iSet = CreateIndexSet(s, p, rSet)
        MineIndexSet(p, iSet)
