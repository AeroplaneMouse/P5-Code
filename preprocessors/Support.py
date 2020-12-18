from models.FState import FState
from models.SState import SState
from models.Interval import Interval


# Tries to find the given state in the support list.
# Returns: index of state if found
#          None if not found
def GetIndex(stateName, stateSupportList):
    index = 0
    for element in stateSupportList:
        if stateName == element.StateName:
            return index
        index += 1
    return None


# Generates a support list from the given temporal database
def GenerateStateSupportList(mdb):
    supportList = []

    # For every client sequence
    clientCount = 0
    for cs in mdb:
        # Update client count
        clientCount += 1

        # For every client record
        for i in range(0, len(cs)):
            clientRecord = cs.iloc[i]

            # Add state to supportList if not counted
            index = GetIndex(clientRecord.State, supportList)
            if index is None:
                supportList.append(SState(
                    stateName=clientRecord.State,
                    appearsIn=[clientCount - 1]))

            # Update state with current clientID if not in AppearsIn
            else:
                if clientRecord.ClientID not in supportList[index].AppearsIn:
                    supportList[index].AppearsIn.append(clientRecord.ClientID)

    # Compute the support for all states
    for state in supportList:
        state.Support = len(state.AppearsIn) / clientCount

    return supportList


def IsSupported(state):
    return


# Removes client records from mdb that does not meet the minimum support
def RemoveNonSupported(minSupport, supportList, mdb):
    # Extract support states from support list
    supportedStates = []
    for s in supportList:
        if s.Support >= minSupport:
            supportedStates.append(s.StateName)

    # In every cs, remove rows where State is not in supportedStates
    for cs in mdb:
        cs.where(cond=cs.State.isin(supportedStates), inplace=True)
        # Remove empty rows made by 'where'
        cs.dropna(inplace=True)
        # Correct indexies
        cs.reset_index(drop=True, inplace=True)

    return mdb


def ExtractInterval(state, cs):
    for cRecord in cs.iterrows():
        if cRecord[1].State == state:
            return Interval(cRecord[1].Start, cRecord[1].End)


def ExtractFrequentStates(minSupport, supportList, mdb):
    states = []

    for s in supportList:
        if s.Support >= minSupport:
            cs = mdb[s.AppearsIn[0]]
            intv = ExtractInterval(s.StateName, cs)
            states.append(FState(s.StateName, intv.Start, intv.End))

    return states
