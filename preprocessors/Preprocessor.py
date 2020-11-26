import pandas as pa
import numpy as np
from logging import *


class GenericPreprocessor:
    def __init__(self, csvPath, seperator, colOfInterest, getState, logger):
        self.logger = logger

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

        self.__getState__ = getState

    def GenerateTemporalMdb(self):
        mdb = []

        # Generate date series
        startDay = self.df.head(1).index[0]
        endDay = self.df.tail(1).index[0]
        days = pa.date_range(start=startDay, end=endDay, freq='D')

        # Setting first clientID
        clientID = 0

        n = len(days)
        progress = 1

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
                cs = self.__generateClientSequence(clientID, data)
                mdb.append(cs)

            # Increment clientID every day
            clientID += 1

            # Logging progress
            procent = (progress / n) * 100
            log = Log('Preprocessing {:.1f}%'.format(procent), Severity.INFO)
            self.logger.log(log)
            progress += 1

        log = Log('Preprocessing finished', Severity.NOTICE)
        self.logger.log(log)
        return mdb, skippedDays

    def __getState(self, value, columnName):
        # Skip empty values
        if (type(value) is np.float64 and np.isnan(value)):
            return None
        else:
            return self.__getState__(value, columnName)

    def __generateClientSequence(self, clientId, data):
        df = pa.DataFrame(columns=['ClientID', 'State', 'Start', 'End'])
        hRegister = {}
        lastIndex = 0

        for row in data.iterrows():
            time = row[0]

            for col in row[1].index:
                state = self.__getState(value=row[1][col], columnName=col)

                # Column information to holding register
                if col not in hRegister:
                    hRegister[col] = {
                        'ClientID': clientId,
                        'State': state,
                        'Start': time,
                        'End': time}

                # Change active state
                elif state != hRegister[col]['State']:
                    # Save endtime for active state
                    hRegister[col]['End'] = time

                    # Insert active state into DataFrame
                    if hRegister[col]['State'] is not None:
                        df = pa.concat([df, pa.DataFrame(data=hRegister[col], index=[lastIndex])])
                        lastIndex += 1

                    # Switch active state to current
                    hRegister[col] = {
                        'ClientID': clientId,
                        'State': state,
                        'Start': time,
                        'End': time}

        # Save end time for remaining active states
        # and insert into DataFrame
        time = data.tail(1).index[0]
        for col in data.columns:
            if hRegister[col]['State'] is not None:
                hRegister[col]['End'] = time
                df = pa.concat([df, pa.DataFrame(data=hRegister[col], index=[lastIndex])])
                lastIndex += 1

        # Sort DataFrame by start and end time
        df.sort_values(by=['Start', 'End'], inplace=True)

        # Fixed indexes
        df.reset_index(drop=True, inplace=True)

        return df
