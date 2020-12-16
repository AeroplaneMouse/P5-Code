from tpmmodels.Endpoint import Endpoint

class TempEP:
    def __init__(self, label, isStart, time):
        self.Label = label
        self.IsStart = isStart
        self.Time = time
        
    def __str__(self):
        return str(self.Label) + 'start: ' + str(self.IsStart) + ' Time: ' + str(self.Time)
        
        
def TDBToEndpointSequenceList(mdb):

    EndpointSequenceList = []

    for element in mdb:
        EndpointSequence = []
        
        TempEPlist = []
        
        i = 0

        #make list of TempEPs.
        while (i < len(element)):
            TempEPlist.append(TempEP(element.at[i,'State'],True,element.at[i,'Start']))
            TempEPlist.append(TempEP(element.at[i,'State'],False,element.at[i,'End']))
            i = i + 1
        
        #sort TempEPs by time.
        TempEPlist.sort(key=lambda x: (x.Time, x.IsStart))
        
        #make EPs for EndpointSequence and add them.
        lastTime = -1
        counted = False
        p = 0
        
        for ep in TempEPlist:
            if(ep.Time == lastTime):
                if(counted == False):
                    p = p + 1
                    EndpointSequence[-1].Parenthesis = p
                    EndpointSequence.append(Endpoint(ep.Label, ep.IsStart, p))
                    counted = True
                else:
                    EndpointSequence.append(Endpoint(ep.Label, ep.IsStart, p))
            else:
                EndpointSequence.append(Endpoint(ep.Label, ep.IsStart, 0))
                lastTime = ep.Time
                counted = False
            
        EndpointSequenceList.append(EndpointSequence)

    return EndpointSequenceList
