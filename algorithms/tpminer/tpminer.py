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
        TempEPlist.sort(key=lambda tempEP: tempEP.Time)
        
        #make EPs for EndpointSequence and add them.
        eps_len = len(TempEPlist)
        i = 0
        while i < eps_len:
            j = 0
            cur_time = TempEPlist[i].Time

            while i+j+1 < eps_len and TempEPlist[i+j+1].Time == cur_time:
                j = j + 1

            if j > 0:
                EndpointSequence.append(set([Endpoint(x.Label, x.IsStart, x.Time) for x in TempEPlist[i:i+j+1]]))
            else:
                EndpointSequence.append(Endpoint(TempEPlist[i].Label, TempEPlist[i].IsStart, TempEPlist[i].Time))
            i = i + j + 1
        
        EndpointSequenceList.append(EndpointSequence)

    print(EndpointSequenceList[0])
    return EndpointSequenceList
