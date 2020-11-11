import pandas as pa


class Preprocessor:
    def __init__(self, csvPath, seperator, colOfInterest):
        # Load data from CSV
        self.df = pa.read_csv(csvPath, sep=seperator)

        # Set timestamps as index and convert to UTC time
        self.df.index = pa.to_datetime(
            self.df.pop('Timestamp'),
            utc=True)

        # Remove unwanted columns
        for col in self.df.columns:
            if col not in colOfInterest:
                self.df.pop(col)

        # Remove timezone data
        self.df = self.df.tz_convert(None)

    def GenerateTemporalMdb(self):
        mdb = []

        # Generate date series
        startDay = self.df.head(1).index[0]
        endDay = self.df.tail(1).index[0]
        days = pa.date_range(start=startDay, end=endDay, freq='D')

        # Setting first clientID
        clientID = 0

        # Generate client sequence for every day
        skippedDays = []
        for day in days:
            # Remove time from date
            day = str(day)[0:10]

            # Get dataframe for current day
            data = self.df[day]

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


def GenerateClientSequence(clientId, data):
    return
