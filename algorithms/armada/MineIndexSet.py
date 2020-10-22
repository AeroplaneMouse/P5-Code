from algorithms.armada.CreateIndexSet import CreateIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada import Storage
from models.PState import PState
from models.FState import FState
from models.Interval import Interval


# Computes new stems
# Assumes that cs only contains states that is above minSup
def ComputePotentialStems(indexSet, minSup):
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
                pStems[csRecord.State] = PState(Interval(csRecord.Start, csRecord.End))

            # Insert clientID if not there
            clientID = csRecord.ClientID
            if clientID not in pStems[csRecord.State].AppearsIn:
                pStems[csRecord.State].AppearsIn.append(clientID)

    # Print pStems content
    # for key in pStems.keys():
    #     print('{} | {}'.format(key, pStems[key]))

    # Add frequent states to stems
    stems = []
    clients = cs[:1].at[0, 'ClientID'] + 1
    for s in pStems:
        support = len(pStems[s].AppearsIn) / clients
        if support >= minSup:
            # Create FState
            intv = pStems[s].Interval
            state = FState(s, intv.Start, intv.End)
            stems.append(state)

    return stems


def MineIndexSet(pattern, indexSet):
    stems = ComputePotentialStems(indexSet, Storage.MinimumSupport)

    for s in stems:
        p_mark = CreatePattern(pattern, s)
        pSet = CreateIndexSet(s, pattern, indexSet)
        MineIndexSet(p_mark, pSet)
