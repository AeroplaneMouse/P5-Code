from typing import Pattern
from models.IndexSet import IndexSet
from models.IndexRecord import IndexRecord
import copy as copy
from algorithms.armada.CreatePattern import CreatePattern
from algorithms.armada import Storage
import numpy as np

# visited_states is used to keep check of frequent patterns that already have an index set
patterns = []

# range set is an index set.
def CreateIndexSet(stem, pattern, range_set):
    p_m_idx = IndexSet(pattern, [])

    csList = []
    isIndexSet = False
    if range_set == Storage.MDB:
        csList = Storage.MDB
        start_pos = 0
    else:
        isIndexSet = True
        for record in range_set.Records:
            cs = Storage.MDB[record.Ref]
            csList.append(cs)

    #Goes through all the client sequences in range_set
    i = 0
    for cs in csList:
        if isIndexSet:
            start_pos = range_set.Records[i].Pos + 1

        pos = start_pos

        #goes through the frequent states in cs
        for pos in range(pos, len(cs)):
            #if the state found is equal the index set pattern add to index set
            if cs.iloc[pos].State == stem.State:
                ref = cs.at[0, 'ClientID']
                intv = [[cs.iloc[pos].Start, cs.iloc[pos].End]]

                new_rec = IndexRecord(pos, intv, ref)
                p_m_idx.Records.append(new_rec)
                break

        i += 1

    patterns.append(p_m_idx.Pattern)
    return p_m_idx


def printPatterns():
    for i in patterns:
        print("Pattern:")
        print(i)
        print()


"""
# MDB is the list of client sequences
# visited_states is used to keep check of frequent states that already have an index set
def CreateFirstIndexSet(stem, visited_states):
    idx = IndexSet(CreatePattern(None, stem.State), [])
    #Checks if a index set is already created
    if stem.State not in visited_states:
        visited_states.append(stem.State)
        #Goes through all the client sequences in mdb
        for cs in Storage.MDB:
            #goes through the frequent states in cs
            for singleState in range(0,len(cs)):
                #if the state found is equal the index set pattern add to index set
                if cs.iloc[singleState].State == stem.State:
                    
                    ref = cs
                    intv = [[cs.iloc[singleState].Start, cs.iloc[singleState].End]]
                    pos = singleState

                    new_rec = IndexRecord(pos, intv, ref)

                    idx.Records.append(new_rec)
                    break
            continue
        return idx
"""