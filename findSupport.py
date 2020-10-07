class StateSupport:
    def __init__(self, stateName, appearsIn):
        self.stateName = stateName
        self.appearsIn = appearsIn
        self.support

def makeStateSupportList(temporalDB):
    #Go through each clientID
    for clientID in temporalDB.ClientID:
        #Save rows in
        Rows = clientID.iterrows()
        Rows
            
        



def findSupport(temporalDB, minsup, StateSupportList):
    
    clientCount = temporalDB.ClientID.tail(1).index[0]
    
    for state in StateSupportList:
        state.support = state.appearsIn.Count / clientCount
    
    
    support = 1
    return support