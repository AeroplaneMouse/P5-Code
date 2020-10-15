class StateSupport:
    def __init__(self, stateName, appearsIn):
        self.StateName = stateName
        self.AppearsIn = appearsIn
        self.Support = None

    def __str__(self):
        return '{} {} {}'.format(
            self.StateName,
            self.AppearsIn,
            self.Support
        )

    def __repr__(self):
        return self.__str__()


def AlreadyCounted(stateName, stateSupportList):
    index = 0
    for element in stateSupportList:
        if stateName == element.StateName:
            return index
        index += 1 

    return None

# Creates a support list from the given client sequence
def MakeStateSupportList(cs):
    stateSupportList = []

    lastIndex = cs.tail(1).index[0]

    # Go through each clientID
    for cID in range(1,cs.ClientID[lastIndex] + 1):
        currentClient = cs.loc[cs['ClientID'] == cID]
        
        for row in currentClient.iterrows():
            # Add new state
            index = AlreadyCounted(row[1].State, stateSupportList)
            if index is None :
                stateSupportList.append(StateSupport(stateName=row[1].State, appearsIn=[cID]))
            
            else:
                # Update state with current cID
                if cID not in stateSupportList[index].AppearsIn:
                    stateSupportList[index].AppearsIn.append(cID)

    return stateSupportList

# Computes the support for every state in the given support list
def ComputeSupport(cs, stateSupportList):
    lastIndex = cs.tail(1).index[0]
    clientCount = cs.at[lastIndex, 'ClientID']

    for state in stateSupportList:
        state.Support = len(state.AppearsIn) / clientCount
