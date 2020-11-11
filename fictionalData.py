import pandas as pa


class Sensor:
    def __init__(self, label, activeDays, periods):
        self.label = label
        self.activeDays = activeDays
        self.periods = periods

    def getState(self, time):
        if time.weekday() in self.activeDays:
            if self.inPeriods(time):
                return 'ON'
        else:
            return 'OFF'

    def inPeriods(self, time):
        # Remove date info for comparison purposes
        onlyTime = str(time)[11:]
        newTime = pa.to_datetime(onlyTime)

        for p in self.periods:
            if newTime < p.start or newTime > p.end:
                return False

        return True


class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def GetInstanceData(time, sensors):
    data = {}

    for s in sensors:
        data[s.label] = s.getState(time)

    print(data)
    import pdb; pdb.set_trace()  # breakpoint 4c0bc949 //

    return data


def GenerateDayData(day, sensors):
    data = []
    minutes = pa.date_range(start=day, periods=1440, freq='T')

    for t in minutes:
        data.append(GetInstanceData(t, sensors))


def toTime(time):
    return pa.to_datetime(time)


# A generator method for generating a fictional dataset for testing
def GenerateFictionalDataCSV(fileName):
    START_DATE = pa.to_datetime('2020-01-01')
    END_DATE = pa.to_datetime('2020-01-07')
    # END_DATE = pa.to_datetime('2020-03-31')

    # STATES = ['LIGHT_ON', 'LIGHT_OFF', 'PC_ON', 'PC_OFF', 'DOOR_OPEN', 'DOOR_CLOSED']

    days = pa.date_range(start=START_DATE, end=END_DATE, freq='d')

    sensors = {
        Sensor('LIGHT', range(0, 6), [Period(toTime('08:00'), toTime('15:00'))]),
        Sensor('PC', range(0, 6), [Period(toTime('08:20'), toTime('14:40'))]),
        Sensor('DOOR', range(0, 6), [
            Period(toTime('07:55'), toTime('08:00')),
            Period(toTime('15:00'), toTime('15:05'))])
    }

    # Generate data for every day
    for day in days:
        data = GenerateDayData(day, sensors)

        print('{} {}'.format(day, data))



# GenerateFictionalDataCSV('TestData.csv')
