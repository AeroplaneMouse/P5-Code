from tpmmodels.Endpoint import Endpoint


def TDBToEndpointSequenceList(mdb):

    EndpointSequenceList = []

    for element in mdb:
        EndpointSequence = []

        p = 1
        i = 0
        j = 0

        lastTime = -1
        counted = False
        
        while (i < len(element)):
            if (element.at[j, 'End'] < element.at[i, 'Start']):
                if(element.at[j,'End']== lastTime):
                    if(counted==True):
                        EndpointSequence.append(Endpoint(element.at[j,'State'], False, p))
                    else:
                        p = p + 1
                        EndpointSequence[-1].Parenthesis = p
                        EndpointSequence.append(Endpoint(element.at[j,'State'], False, p))
                        counted = True
                else:
                    EndpointSequence.append(Endpoint(element.at[j,'State'], False, 0))
                    lastTime = element.at[j,'End']
                    counted = False
                j += 1
                
            else:
                if(element.at[i,'Start'] == lastTime):
                    if(counted == True):
                        EndpointSequence.append(Endpoint(element.at[i,'State'], True, p))
                    else:
                        p = p + 1
                        EndpointSequence[-1].Parenthesis = p
                        EndpointSequence.append(Endpoint(element.at[i,'State'], True, p))
                        counted = True
                else:
                    EndpointSequence.append(Endpoint(element.at[i,'State'], True, 0))
                    lastTime = element.at[i,'Start']
                    counted = False
                i += 1
                
        while (j<len(element)):
            if(element.at[j,'End']== lastTime):
                if(counted==True):
                    EndpointSequence.append(Endpoint(element.at[j,'State'], False, p))
                else:
                    p = p + 1
                    EndpointSequence[-1].Parenthesis = p
                    EndpointSequence.append(Endpoint(element.at[j,'State'], False, p))
                    counted = True
            else:
                EndpointSequence.append(Endpoint(element.at[j,'State'], False, 0))
                lastTime = element.at[j,'End']
                counted = False
            j += 1
        
        EndpointSequenceList.append(EndpointSequence)
        
        
        # while (i < len(element)):
        #     # if (element.at[j, 'End'] == element.at[i, 'Start']):
        #     #     # create a parenthesis pair of endpoints
        #     #     EndpointSequence.append(Endpoint(element.at[i,'State'], True, p))
        #     #     EndpointSequence.append(Endpoint(element.at[j,'State'], False, p))
        #     #     # count up i,j, and parenthesis counter
        #     #     p += 1
        #     #     i += 1
        #     #     j += 1

        #     if (element.at[j, 'End'] < element.at[i, 'Start']):
        #         # create a finishing endpoint for j, and append to Endpoint Sequence.
        #         EndpointSequence.append(Endpoint(element.at[j,'State'], False, 0))
        #         # count up j
        #         j += 1
        #     else:
        #         # Create a starting endpoint for i, and append to Endpoint Sequence.
        #         EndpointSequence.append(Endpoint(element.at[i,'State'], True, 0))
        #         # count up i
        #         i += 1

        # while (j<len(element)):
        #     # create remaining endpoints for finishing endpoints
        #     EndpointSequence.append(Endpoint(element.at[j,'State'], False, 0))
        #     # count up j
        #     j += 1
        

        # EndpointSequenceList.append(EndpointSequence)



    return EndpointSequenceList
