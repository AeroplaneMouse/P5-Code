import pandas as pa
import numpy as np


class VentPreprocessor:
    def __init__(self, csvPath, seperator):
        # Load data from
        self.DataFrame = pa.read_csv(csvPath, sep=seperator)

        # Set timestamps as index and convert to UTC time
        self.DataFrame.index = pa.to_datetime(
            self.DataFrame.pop('Timestamp'), 
            utc=True)

        # Remove shitty columns
        self.DataFrame.pop('DayOfWeek')
        self.DataFrame.pop('TimeStamp_Count')
        self.DataFrame.pop('Vent_HRVstaleairpressuredifferential')
        self.DataFrame.pop('Vent_HRVfreshairpressuredifferential')

        # Remove timezone data
        self.DataFrame = self.DataFrame.tz_convert(None)

    def GenerateTemporalMdb(self, interval):
        mdb = []

        # Generate date series
        startDay = self.DataFrame.head(1).index[0]
        endDay = self.DataFrame.tail(1).index[0]
        days = pa.date_range(start=startDay, end=endDay, freq='D')

        skippedDays = []

        # Setting first clientID
        clientID = 0

        for day in days:
            # Remove time from date
            day = str(day)[0:10]

            # Get dataframe for current day
            data = self.DataFrame[day]

            # Check if day is empty
            if data.empty:
                skippedDays.append(day)
                continue  # Don't increment clientID for empty days
            else:
                mdb.append(GenerateClientSequence(
                    clientID,
                    data,
                    interval))

            # Increment clientID every day
            clientID += 1

        return mdb, skippedDays


# Computes the state given a value and the interval for each state
def GetState(value, interval):
    # Compute distance to range start
    r = value % interval

    # Compute range start and end
    rangeStart = value - r
    rangeEnd = rangeStart + interval

    return '{:.0f}->{:.0f}'.format(
        rangeStart,
        rangeEnd)


def SwitchActiveState(newState, columnIndex, time, clientID, hRegister, df):
    # Check if hRegister contains key for column.
    # Then save end for active state
    if str(columnIndex) + 'CurState' in hRegister:
        index = hRegister[str(columnIndex) + 'CurIndex']
        df.at[index, 'End'] = time  # Overwrites first endtime

    # Insert new state into df
    lastIndex = None
    if df.empty:
        lastIndex = 0
    else:
        lastIndex = df.tail(1).index[0] + 1

    # Insert new record
    data = {'ClientID': [clientID],
            'State': ['{}_{}'.format(columnIndex, newState)],
            "Start": [time],
            'End': [time]}
    df = pa.concat([df, pa.DataFrame(data=data, index=[lastIndex])])

    # Update hRegister
    hRegister[str(columnIndex) + 'CurState'] = newState
    hRegister[str(columnIndex) + 'CurIndex'] = lastIndex

    return df


# Creates temporal client sequence for one clientID(day)
def GenerateClientSequence(clientID, data, interval):
    hRegister = {}
    df = pa.DataFrame(columns=['ClientID', 'State', 'Start', 'End'])

    index = -1
    for row in data.iterrows():
        index += 1
        timeIndex = row[0]

        # Go through each column and compare active and current state
        c = 0
        for cValue in row[1].array:
            # Check column value
            if not np.isnan(cValue):
                state = GetState(cValue, interval)

                # Switch active state for current column
                if str(c) + 'CurState' not in hRegister or state != hRegister[str(c) + 'CurState']:
                    df = SwitchActiveState(
                        newState=state,
                        columnIndex=c,
                        time=timeIndex,
                        clientID=clientID,
                        hRegister=hRegister,
                        df=df
                    )

            # Increment column index
            c += 1

    # End remaining states
    c = 0
    time = data.tail(1).index[0]
    for col in data.columns:
        index = hRegister['{}CurIndex'.format(c)]
        df.at[index, 'End'] = time
        c += 1

    df.sort_values(by=['Start', 'End'], inplace=True)
    return df