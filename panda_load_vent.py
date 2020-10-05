import pandas as pa

path = 'datasets/%s.csv'
datasetName = 'vent-minute-short'


# Create states
def create_states():
    states = {}
    value = MIN_VALUE

    while value < MAX_VALUE:
        states[value] = str(value) + " -> " + str(value + INCREMENT)
        value += INCREMENT

    return states

# Maps a value to a state
def get_state(value, states):
    interval = MIN_VALUE

    while interval < value:
        interval += INCREMENT
    interval -= INCREMENT

    return states[interval]







# Create DataFrame
vent = pa.read_csv(path % datasetName, header=0, sep=';')

# Remove timestamp column from dataset and use as index
vent.index = pa.to_datetime(vent.pop('Timestamp'))

print(vent.Vent_HRVTempExhaustOut['2013-07-01 00:01:14-04:00'])



print('Done')