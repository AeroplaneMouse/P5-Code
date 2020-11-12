import pandas as pa
from os import path


class Sensor:
    def __init__(self, label, activeDays, periods):
        self.label = label
        self.activeDays = activeDays
        self.periods = periods

    def getState(self, time):
        if time.weekday() in self.activeDays and self.inPeriods(time):
            return 'ON'
        else:
            return 'OFF'

    def inPeriods(self, time):
        # Remove date info for comparison purposes
        onlyTime = str(time)[11:]
        newTime = pa.to_datetime(onlyTime)

        for p in self.periods:
            if newTime >= p.start and newTime <= p.end:
                return True

        return False


class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Generate the instance data for every sensor at the given time
def GetInstanceData(time, sensors):
    data = {'Timestamp': time}
    for s in sensors:
        data[s.label] = s.getState(time)

    return data


def GenerateDayData(day, sensors):
    data = []
    minutes = pa.date_range(start=day, periods=1440, freq='T')

    for t in minutes:
        data.append(GetInstanceData(t, sensors))

    return data


def toTime(time):
    return pa.to_datetime(time)


def generateFirstRow(sensors):
    firstRow = {'Timestamp': 'Timestamp'}

    for s in sensors:
        firstRow[s.label] = s.label

    return firstRow


def createFile(fileName):
    if path.exists(fileName):
        print('Found existing dataset with name \'' + fileName + '\'. Overwriting...')
    else:
        print('Creating dataset \'' + fileName + '\'')

    return open(fileName, 'wt')


# Writes data to file
def insert(file, dataRow):
    i = 0
    lastKey = None
    for key in dataRow:
        if i >= len(dataRow) - 1:
            lastKey = key
            break

        data = str(dataRow[key]) + '; '
        file.write(data)
        i += 1

    # Write last row to file
    data = str(dataRow[lastKey]) + '\n'
    file.write(data)


# A generator method for generating a fictional dataset for testing
def GenerateFictionalDataCSV(fileName):
    START_DATE = pa.to_datetime('2020-01-01')
    END_DATE = pa.to_datetime('2020-01-07')
    # END_DATE = pa.to_datetime('2020-03-31')

    # STATES = ['LIGHT_ON', 'LIGHT_OFF', 'PC_ON', 'PC_OFF', 'DOOR_OPEN', 'DOOR_CLOSED']

    days = pa.date_range(start=START_DATE, end=END_DATE, freq='d')

    sensors = {
        Sensor('LIGHT', range(0, 5), [Period(toTime('08:00'), toTime('15:00'))]),
        Sensor('PC', range(0, 5), [Period(toTime('08:20'), toTime('14:40'))]),
        Sensor('DOOR', range(0, 5), [
            Period(toTime('07:55'), toTime('08:00')),
            Period(toTime('15:00'), toTime('15:05'))])
    }

    file = createFile(fileName)

    firstRow = generateFirstRow(sensors)
    insert(file, firstRow)

    # Generate data for every day
    for day in days:
        data = GenerateDayData(day, sensors)
        for d in data:
            insert(file, d)

    file.close()


if __name__ == '__main__':
    GenerateFictionalDataCSV('datasets/TestData.csv')
