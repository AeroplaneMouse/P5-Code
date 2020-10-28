from algorithms.armada.CreateIndexSet import CreateIndexSet
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada import Storage
from models.PState import PState
from models.FState import FState
from models.Interval import Interval
import numpy as np


def GetFirstEndTime(pattern):
    # Extract states
    states = pattern[0][1:]

    # Use first state as initial end time
    time = states[0].End

    for s in states[1:]:
        if s.End < time:
            time = s.End

    return time


def ExtractStatesInPattern(pattern):
    states = []
    dim = np.shape(pattern)[0]

    for i in range(1, dim):
        states.append(pattern[0][i].State)

    return states


# Computes new stems
# Assumes that cs only contains states that is above minSup
def ComputePotentialStems(indexSet, minSup, maxGap):
    # Dictionary of potential stems
    pStems = {}

    time = GetFirstEndTime(indexSet.Pattern)

    for record in indexSet.Records:
        # Retrieve cs from reference
        cs = Storage.MDB[record.Ref]

        # Increment support count for every state in cs
        # after pos in indexSet record
        for csIndex in range(record.Pos + 1, len(cs)):
            csRecord = cs.iloc[csIndex]

            # Check if stem is within max gap constraint
            if csIndex.End < time + maxGap:
                # Insert state into stem if not there
                if csRecord.State not in pStems:
                    pStems[csRecord.State] = PState(Interval(csRecord.Start, csRecord.End))

                # Insert clientID if not there
                clientID = csRecord.ClientID
                if clientID not in pStems[csRecord.State].AppearsIn:
                    pStems[csRecord.State].AppearsIn.append(clientID)

    # Add frequent states to stems
    stems = []
    clients = len(Storage.MDB)
    patternStates = ExtractStatesInPattern(indexSet.Pattern)
    for s in pStems:
        # Only add states not already part of the pattern
        if s not in patternStates:
            # Compute stem support
            support = len(pStems[s].AppearsIn) / clients
            
            # Add frequent stems to output
            if support >= minSup:
                intv = pStems[s].Interval
                state = FState(s, intv.Start, intv.End)
                stems.append(state)

    return stems


def MineIndexSet(pattern, indexSet):
    stems = ComputePotentialStems(indexSet, Storage.MinimumSupport, Storage.MaximumGap)

    # Create and mine index sets for the new pattern p_mark
    for s in stems:
        # Create and save pattern
        p_mark = CreatePattern(pattern, s)
        Storage.Patterns.append(p_mark)

        pSet = CreateIndexSet(s, p_mark, indexSet)
        MineIndexSet(p_mark, pSet)
