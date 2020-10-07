import pandas as pa

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

def CreateTimeSeries(clientID, data):
    
    for d in data.iterrows():
        print('Index: {:>30}'.format(str(d[0])))
        
        for column in d[1].array:
            print(column)
        break