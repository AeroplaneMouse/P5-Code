import pandas as pa
from generators.stateGenerator import StateGenerator

class VentPreprocessor:
    DataFrame = None


    def CreateDataFrame(self, csvPath, seperator):
        # Load data from
        self.DataFrame = pa.read_csv(csvPath, sep=seperator)

        # Set timestamps as index
        self.DataFrame.index = pa.to_datetime(self.DataFrame.pop('Timestamp'))

        # Remove shitty columns
        self.DataFrame.pop('DayOfWeek')
        self.DataFrame.pop('TimeStamp_Count')
        self.DataFrame.pop('Vent_HRVstaleairpressuredifferential')
        self.DataFrame.pop('Vent_HRVfreshairpressuredifferential')

        # Remove timezone
        self.DataFrame = self.DataFrame.tz_convert(None)


    def GetTemporalDataFrame(self):
        df = pa.DataFrame(columns=['ClientID', 'State', 'Start', 'End'])

        # Generate date series
        startDay = self.DataFrame.head(1).index[0]
        endDay = self.DataFrame.tail(1).index[0]
        days = pa.date_range(start=startDay, end=endDay, freq='D')

        clientID = 1
        for day in days:
            # Remove time from date
            day = str(day)[0:10]

            # Append dataframe for current day
            df = df.append(
                CreateTimeSeries(clientID, self.DataFrame[day]),
                ignore_index=True
            )

            # print(df)

            # Increment clientID every day
            clientID += 1
            break


        return df


# Maps a value to a state from the StateGenerator
def GetState(value, stateGen):
    # Generate states if none
    if stateGen.LastStates is None:
        stateGen.GenerateStates()

    interval = stateGen.MinValue

    while interval < value:
        interval += stateGen.Increment
    interval -= stateGen.Increment

    return stateGen.LastStates[interval]

def SwitchActiveState(newState, columnIndex, time, hRegister, df):
    # Check if hRegister contains key for column
    if str(columnIndex) + 'CurState' in hRegister:
        # Save active state
        index = hRegister[str(columnIndex) + 'CurIndex']
        df.at[index, 'End'] = time
    

    # Insert new state into df
    index = df.insert()

    # Update hRegister
    hRegister[str(columnIndex) + 'CurState'] = newState
    hRegister[str(columnIndex) + 'CurIndex'] = index

    return

# Creates temporal client sequence for one clientID(day)
def CreateTimeSeries(clientID, data):
    stateGen = StateGenerator(minValue=-50, maxValue=50, increment=5)
    hRegister = {}
    df = pa.DataFrame(columns=['ClientID', 'State', 'Start', 'End'])

    for row in data.iterrows():
        timeIndex = row[0]

        # Go through each column and compare active and current state
        c = 0
        for cValue in row[1].array:
            state = GetState(cValue, stateGen)

            # Switch active state for current column
            if str(c) + 'CurState' not in hRegister or state != hRegister[str(c) + 'CurrentState'] is KeyError:
                SwitchActiveState(
                    newState=state,
                    columnIndex=c,
                    time=timeIndex,
                    hRegister=hRegister
                )

            # Increment column index
            c += 1

            print(c)
        break