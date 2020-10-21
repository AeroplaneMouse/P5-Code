class StateSupport:
    def __init__(self, stateName, appearsIn):
        self.StateName = stateName
        self.AppearsIn = appearsIn
        self.Support = None

    def __str__(self):
        return '{} | {:<10} | {:.2f}'.format(
            self.StateName,
            str(self.AppearsIn),
            self.Support
        )

    def __repr__(self):
        return self.__str__()


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
                supportList.append(StateSupport(
                    stateName=clientRecord.State,
                    appearsIn=[clientRecord.ClientID]))

            # Update state with current clientID if not in AppearsIn
            else:
                if clientRecord.ClientID not in supportList[index].AppearsIn:
                    supportList[index].AppearsIn.append(clientRecord.ClientID)

    # Compute the support for all states
    for state in supportList:
        state.Support = len(state.AppearsIn) / clientCount

    return supportList
