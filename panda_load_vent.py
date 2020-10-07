import pandas as pa
import numpy as np

MIN_VALUE = -50
MAX_VALUE = 50
INCREMENT = 5

path = 'datasets/%s.csv'
datasetName = 'vent-minute-short'



##################################################

class State:
    def __init__(self, minValue, maxValue):
        self.MinValue = minValue
        self.MaxValue = maxValue

    def __str__(self):
        return str(self.MinValue) + ' -> ' + str(self.MaxValue)

class StateSpan:
    def __init__(self, clientID, state, startTime, endTime):
        self.ClientID = clientID
        self.State = state
        self.Start = startTime
        self.End = endTime

    def __str__(self):
        output = '{:>8} | {:>8} | {:>20} | {:>20}'.format(
            str(self.ClientID),
            str(self.State),
            str(self.Start),
            str(self.End)
        )
        return output


##################################################


# Create states
def create_states():
    states = {}
    value = MIN_VALUE

    while value < MAX_VALUE:
        # states[value] = State(value, value + INCREMENT)
        states[value] = str(value) + " -> " + str(value + INCREMENT)
        value += INCREMENT

    return states

# Maps a value to a state
def get_state(value, states):
    interval = MIN_VALUE

    while interval < value:
        interval += INCREMENT
    interval -= INCREMENT

    return states[interval]


# def generateSequence(sensorSeries, clientID):
#     sequence = []
#     states = create_states()

#     currentState = get_state(sensorSeries[0], states)
#     startIndex = sensorSeries.index[0]
#     lastIndex = 0

#     for value in sensorSeries[1:]:
#         # Get state for current value
#         state = get_state(value, states)
        
#         # Compare current value with last
#         if state != currentState:
#             # End last state and add to list
#             sequence.append(StateSpan(
#                 clientID, 
#                 state=currentState, 
#                 startTime=startIndex, 
#                 endTime=sensorSeries.index[lastIndex]))

#             # Set next
#             currentState = state
#             startIndex = sensorSeries.index[lastIndex + 1]

#         # Update last index
#         lastIndex += 1

#     return sequence

def getValue(record, column):
    return record[column][0]

def createTimeSeries(clientID, data):
    # f2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
    # df.append(df2)
    # d = {'col1': [1, 2], 'col2': [3, 4]}
    # df = pa.DataFrame(data=d)




    # df2 = pa.DataFrame([['1', 'A', '2', '2'],['2', 'B', '3', '4']], columns=['ClientID','State','Start','End'])
    # dataFrame = dataFrame.append(df2, ignore_index=True)
    



    ## THe following code is not final and should/must be changed.
    ## This was for testing and learning purposes.

    states = create_states()
    firstRow = data.head(1)

    # Initiate holding register and time series
    nextIndex = 0
    holdingRegister = {}
    timeSeries = []
    for sensor in data.columns:
        # Holding register
        holdingRegister[sensor + 'CurrentIndex'] = nextIndex
        holdingRegister[sensor + 'CurrentState'] = get_state(getValue(firstRow, sensor), states)

        # Time series
        timeSeries.append([[
            clientID, 
            holdingRegister[sensor + 'CurrentState'], 
            firstRow.index[0], 
            None
        ]])

        # Update nextIndex
        nextIndex += 1

    # print(data.index[31])
    # return

    # Fill time series
    currentRow = 0
    for record in data.values[1:]:
        currentSensorIndex = 0
        # For every sensor, check if a new series starts
        for value in record:
            currentSensor = data.columns[currentSensorIndex]
            state = get_state(value, states)
            if state != holdingRegister[currentSensor + 'CurrentState']:
                # Save end time for current state
                index = holdingRegister[currentSensor + 'CurrentIndex']
                timeSeries[index][3] = data.index[currentRow]

                # Start new state and save in holding register
                holdingRegister[currentSensor + 'CurrentIndex'] = nextIndex
                holdingRegister[sensor + 'CurrentState'] = get_state(value, states)
                timeSeries.append([[
                    clientID, 
                    holdingRegister[currentSensor + 'CurrentState'], 
                    data.index[currentRow], 
                    None
                ]])

                # Update nextIndex
                nextIndex += 1


            currentSensorIndex += 1
        currentRow += 1
        print(currentRow)

    print(timeSeries)

    # Print holding register values
    # for d in holdingRegister:
    #     print('{:>40} {:<20}'.format(d, holdingRegister[d]))

    # Print time series
    # for record in timeSeries:
    #     print(record)



    # print(df)
    # return df


# Import data, create Pandas dataframe
vent = pa.read_csv(path % datasetName, header=0, sep=';')

# Set timestamps as index
vent.index = pa.to_datetime(vent.pop('Timestamp'))

# Remove shitty columns
vent.pop('DayOfWeek')
vent.pop('TimeStamp_Count')
vent.pop('Vent_HRVstaleairpressuredifferential')
vent.pop('Vent_HRVfreshairpressuredifferential')

# Remove timezone
vent = vent.tz_convert(None)

# Generate date series
startDay = vent.head(1).index[0]
endDay = vent.tail(1).index[0]
days = pa.date_range(start=startDay, end=endDay, freq='D')

# print('{:>8} | {:>8} | {:>20} | {:>20}'.format(
#     'ClientID',
#     'State',
#     'StartTime',
#     'EndTime'
#     ))

temporalDF = pa.DataFrame(columns=['ClientID', 'State', 'Start', 'End'])
clientID = 1

for day in days:
    # Remove time from date
    day = str(day)[0:10]

    temporalDF = temporalDF.append(
        createTimeSeries(clientID, vent[day]),
        ignore_index=True)

    # print(temporalDF)
    break

    # Increse client ID
    clientID += 1






# Convert temperatures to states
# states = create_states()
# sensors = vent.columns[2:0]
# ventTemporal = pa.DataFrame()


# for s in sensors:
#     sensorData = vent.pop(s)
#     # span = [sensorData.head(1), sensorData.tail(1)]
#     # get_days(span)
#     for day in get_days(span):
#         print(sensorData[day])

    # break
    
    # # print(sensorData.head(20))
    # print(sensorData['2013-07-01'])
    # print(sensorData.between_time('00:00:00', '23:59:59'))




    # sensorData = vent.pop(s)
    # index = 0
    # for data in sensorData:
    #     sensorData[index] = get_state(data, states)
    #     index += 1

    # print(sensorData.head(10))
    # vent.
    # print(sensorData.head(2))
    # print()
    


# print(vent.dtypes)

#print(vent.)
#print(vent.Vent_HRVTempExhaustOut['2013-07-01 00:01:14'])

 # pd.to_datetime(['04-01-2012 10:00'], dayfirst=True)

# ClientID | State | start | end



