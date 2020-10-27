from algorithms.armada.CreateIndexSet import CreateIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada import Storage
from models.PState import PState
from models.FState import FState
from models.Interval import Interval
import numpy as np


def ExtractStatesInPattern(pattern):
    states = []
    dim = np.shape(pattern)[0]

    for i in range(1, dim):
        states.append(pattern[0][i].State)

    return states


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
    clients = len(Storage.MDB)
    patternStates = ExtractStatesInPattern(indexSet.Pattern)
    for s in pStems:
        if s not in patternStates:
            support = len(pStems[s].AppearsIn) / clients
            if support >= minSup:
                # Create FState
                intv = pStems[s].Interval
                state = FState(s, intv.Start, intv.End)
                stems.append(state)

    return stems


def MineIndexSet(pattern, indexSet, depth):
    if depth == -1:
        return

    stems = ComputePotentialStems(indexSet, Storage.MinimumSupport)

    for s in stems:
        p_mark = CreatePattern(pattern, s)
        pSet = CreateIndexSet(s, p_mark, indexSet)
        MineIndexSet(p_mark, pSet, depth+1)
