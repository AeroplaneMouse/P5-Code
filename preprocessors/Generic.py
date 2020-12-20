import numpy as np
import pandas as pa
from logging2 import *
from os import path

PROCESSED_PREFIX = 'processed_'

class GenericPreprocessor:
    mdb = None

    def __init__(self, csvPath, seperator, colOfInterest, getState, logger, timestamp='Timestamp'):
        self.logger = logger
        log = Log('Initializing Generic Preprocessor', Severity.NOTICE)
        self.logger.log(log)

        # Check if file exists
        if not path.exists(csvPath):
            self.logger.log(Log('Dataset not found: {}'.format(csvPath), Severity.ERROR))
            return

        # Check if dataset has already been preprocessed
        self.folder, self.filename = extractFolderFile(csvPath)
        if not path.exists(self.folder + PROCESSED_PREFIX + self.filename):
            # Load data from CSV
            self.df = pa.read_csv(csvPath, sep=seperator)

            # Set timestamps as index and convert to UTC time
            self.df.index = pa.to_datetime(
                self.df.pop(timestamp),
                utc=True)

            # Remove unwanted columns
            for col in self.df.columns:
                if col not in colOfInterest:
                    self.df.pop(col)

            # Remove timezone data
            self.df = self.df.tz_convert(None)

            self.__getState__ = getState

        # Load preprocessed dataset
        else:
            self.logger.log(Log('Found preprocessed data for dataset: ' + self.filename, Severity.NOTICE))
            self.mdb = loadMdbFromFile(self.folder + PROCESSED_PREFIX + self.filename)


    def GenerateTemporalMdb(self):
        if self.mdb is None:
            self.logger.log(Log('Preprocessing started on: ' + self.filename, Severity.NOTICE))
            mdb = []

            # Generate date series
            startDay = self.df.head(1).index[0]
            endDay = self.df.tail(1).index[0]
            days = pa.date_range(start=startDay, end=endDay, freq='D')

            # Setting first clientID
            clientID = 0

            n = len(days)
            progress = 1
            self.logger.log(ProgressLog('Preprocessing:', progress=0))

            # Generate client sequence for every day
            skippedDays = []
            for day in days:
                # Remove time from date
                day = str(day)[0:10]

                # Get dataframe for current day
                data = self.df.loc[day]

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
                procent = progress / n
                self.logger.log(ProgressLog('Preprocessing:', progress=procent))
                progress += 1

            self.logger.log(Log('Preprocessing finished', Severity.NOTICE))

            saveMdbToFile(mdb, self.folder, self.filename, PROCESSED_PREFIX)

        else:
            mdb = self.mdb
            skippedDays = []
            self.logger.log(Log('Loaded preprocessed data', Severity.NOTICE))

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
        endDate = str(data.tail(1).index[0])[:10]
        endTime = pa.to_datetime(endDate + ' 23:59:00')
        for col in data.columns:
            if hRegister[col]['State'] is not None:
                hRegister[col]['End'] = endTime

                # Only add states that did not start in the last minute of the day
                if hRegister[col]['Start'] != hRegister[col]['End']:
                    df = pa.concat([df, pa.DataFrame(data=hRegister[col], index=[lastIndex])])
                    lastIndex += 1

        # Sort DataFrame by start and end time
        df.sort_values(by=['Start', 'End'], inplace=True, ignore_index=True)

        return df


def extractFolderFile(csvPath):
    parts = csvPath.split('/')

    filename = parts[-1:][0]
    folder = ""

    # Extract folders
    if len(parts) > 1:
        for dirName in parts[:-1]:
            folder += dirName + '/'

    return folder, filename


def saveMdbToFile(mdb, folder, filename, prefix):
    index = pa.Int64Index(data=[], name='ClientID')
    combined = pa.DataFrame(index=index, columns=['Indexes', 'State', 'Start', 'End'])

    # Combine all cs's to one DataFrame
    for cs in mdb:
        copyCS = cs.copy(deep=True)
        copyCS['Indexes'] = copyCS.index
        copyCS.index = copyCS.pop('ClientID')
        combined = pa.concat([combined, copyCS])


    combined.to_csv(folder + prefix + filename)


def loadMdbFromFile(filepath):
    processedData = pa.read_csv(filepath)

    # Use ClientID as index
    processedData.index = processedData.pop('ClientID')

    clientIDs = processedData.index.drop_duplicates().tolist()

    # Extract mdb
    mdb = []
    for i in clientIDs:
        cs = processedData.loc[i].copy(deep=True)

        if type(cs) is pa.Series:
            d = {
                'ClientID': i,
                'State': cs['State'],
                'Start': cs['Start'],
                'End': cs['End']}
            cs = pa.DataFrame(data=d, index=[0])
        else:
            cs['ClientID'] = pa.to_numeric(cs.index)
            cs.index = pa.to_numeric(cs.pop('Indexes'))
            cs['Start'] = pa.to_datetime(cs.pop('Start'))
            cs['End'] = pa.to_datetime(cs.pop('End'))

        mdb.append(cs)

    return mdb