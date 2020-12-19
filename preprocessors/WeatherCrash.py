import pandas as pa
from os import path
from logging2 import *
from preprocessors import columns
from preprocessors.Generic import *

class WeatherCrashPreprocessor:
    mdb = None

    def __init__(self, weatherPath, crashPath, logger):
        self.logger = logger
        self.logger.log(Log('Initializing Weather Crash Preprocessor', Severity.NOTICE))

        # Check if dataset has already been preprocessed
        self.folder = extractFolderFile(weatherPath)[0]
        self.filename = 'Weather-Crash.csv'
        if not path.exists(self.folder + PROCESSED_PREFIX + self.filename):
            # Load dataset to be preprocessed
            self.weather = GenericPreprocessor(
                weatherPath,
                ',',
                columns.weather_columns,
                weather_getState,
                logger,
                'pickup_datetime')

            self.df_crash = pa.read_csv(crashPath, sep=',', low_memory=False)

            # Remove columns from crash
            for col in self.df_crash.columns:
                if col not in columns.crash_columns:
                    self.df_crash.pop(col)

            firstDate, lastDate = extractFirstAndLastDate(self.weather)

            # Combining date and time on crash
            self.df_crash.index = pa.to_datetime(self.df_crash.pop('CRASH DATE'), utc=True)
            self.df_crash['CRASH TIME'] = self.df_crash['CRASH TIME'].add(':00')
            self.df_crash = self.df_crash.tz_convert(None)

            # Truncate crashes before and after weather data
            self.df_crash.sort_index(ascending=True, inplace=True)
            self.df_crash = self.df_crash.truncate(before=firstDate, after=lastDate, copy=False)

        else:
            self.logger.log(Log('Found preprocessed data for dataset: ' + self.filename, Severity.NOTICE))
            self.mdb = loadMdbFromFile(self.folder + PROCESSED_PREFIX + self.filename)


    def GenerateTemporalMdb(self):
        if self.mdb is None:
            self.logger.log(Log('Preprocessing started', Severity.NOTICE))

            # Preprocesses weather
            mdb, skippedDays = self.weather.GenerateTemporalMdb()

            self.logger.log(ProgressLog('Preprocessing:', progress=0))
            total = len(mdb)
            current = 1

            # Insert crash data into mdb
            combinedMdb = []
            for cs in mdb:
                # Extract date only
                date = str(cs.at[0, 'Start'])[:10]

                crashes = self.df_crash.loc[date]

                # Convert to TDB
                crashes['ClientID'] = cs.at[0, 'ClientID']
                crashes['State'] = 'Crash'
                crashes['Start'] = crashes.index + pa.to_timedelta(crashes['CRASH TIME'])
                crashes['End'] = crashes['Start'] + pa.to_timedelta('00:01:00')
                # crashes.index = range(len(cs), len(crashes) + 1)
                crashes.pop('CRASH TIME')

                # Insert into weather DataFrame
                combinedCS = pa.concat([cs, crashes], ignore_index=True)
                combinedCS['Start'] = pa.to_datetime(combinedCS['Start'])
                combinedCS['End'] = pa.to_datetime(combinedCS['End'])
                combinedCS.sort_values(by=['Start', 'End'], inplace=True, ignore_index=True)
                combinedMdb.append(combinedCS)

                self.logger.log(ProgressLog('Preprocessing:', progress=(current/total)))
                current += 1

            mdb = combinedMdb
            saveMdbToFile(mdb, self.folder, self.filename, PROCESSED_PREFIX)

        else:
            mdb = self.mdb
            skippedDays = []
            self.logger.log(Log('Loaded preprocessed data', Severity.NOTICE))

        return mdb, skippedDays


def extractFirstAndLastDate(preprocessor):
    if preprocessor.mdb is None:
        firstDate = preprocessor.df.head(1).index[0]
        lastDate = preprocessor.df.tail(1).index[0]
    else:
        firstDate = preprocessor.mdb[0].at[0, 'Start']
        lastDate = preprocessor.mdb[-1:][0].at[0, 'Start']

    # Remove time dates
    firstDate = pa.to_datetime(str(firstDate)[:10])
    lastDate = pa.to_datetime(str(lastDate)[:10])

    return firstDate, lastDate


def weather_getState(value, columnName):
    if value == 1 or value == '1':
        return columnName
    else:
        return None
