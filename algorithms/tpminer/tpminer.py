from tpmmodels import Endpoint


def TDBToEndpointSequenceList(mdb):
    
    EndpointSequenceList = []
    
    for element in mdb:
        EndpointSequence = []
        
        i = element.at[0, 'Start']
        j = element.at[0, 'End']
        
        while (i<len(element)):
            if (element.at[j,'End'] == element.at[i, 'Start']):
                # create a parenthesis pair of endpoints
                # count up i,j
                i += 1
                j += 1
                
            elif (element.at[j,'End'] < element.at[i, 'Start']):
                # create a finishing endpoint for j, and append to Endpoint Sequence.
                
                # count up j
                j += 1
            else:
                # Create a starting endpoint for i, and append to Endpoint Sequence.
                # count up i
                i += 1
        
        while (j<len(element)):
            # create remaining endpoints for finishing endpoints
            # count up j
            j += 1
        
        EndpointSequenceList.Append(EndpointSequence)
        
    
    
    return EndpointSequenceList
        