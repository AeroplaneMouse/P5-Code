import pandas as pa
from preprocessors.loadData import goodColumns


class LoadPreprocessor:
    def __init__(self, csvPath, seperator):
        # Load data from CSV
        self.Load = pa.read_csv(csvPath, sep=seperator)

        # Set timestamps as index and convert to UTC time
        self.Load.index = pa.to_datetime(
            self.Load.pop('Timestamp'),
            utc=True)

        # Remove shitty columns
        for col in self.Load.columns:
            if col not in goodColumns:
                self.Load.pop(col)

        # Remove timezone data
        self.Load = self.Load.tz_convert(None)

    def GenerateTemporalMdb(self):
        mdb = []

        # Generate date series
        startDay = self.Load.head(1).index[0]
        endDay = self.Load.tail(1).index[0]
        days = pa.date_range(start=startDay, end=endDay, freq='D')

        # Setting first clientID
        clientID = 0

        # Generate client sequence for every day
        skippedDays = []
        for day in days:
            # Remove time from date
            day = str(day)[0:10]

            # Get dataframe for current day
            data = self.Load[day]

            # Check if day is empty
            if data.empty:
                skippedDays.append(day)
                continue  # Don't increment clientID for empty days
            else:
                mdb.append(GenerateClientSequence(
                    clientID,
                    data))

            # Increment clientID every day
            clientID += 1

        return mdb, skippedDays


def GetState(value, columnName):
    if value == 1:
        value = 'ON'
    else:
        value = 'OFF'
    return '{}_{}'.format(columnName[11:], value)


def GenerateClientSequence(clientId, data):
    df = pa.DataFrame(columns=['ClientID', 'State', 'Start', 'End'])

    for row in data.iterrows():
        time = row[0]

        for col in row[1].index:
            state = GetState(value=row[1][col], columnName=col)


        import pdb; pdb.set_trace()  # breakpoint 9b4cff7a //

    df.sort_values(by=['Start', 'End'], inplace=True)
    return df
