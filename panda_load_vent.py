import pandas as pa


path = 'C:/Users/danie/OneDrive/AAU/P5/P5-Code/datasets/%s.csv'
datasetName = 'vent-minute'

# Create DataFrame
vent = pa.read_csv(path % datasetName, header=0, sep=';')

# Remove timestamp column from dataset and use as index
# vent.index = pa.to_datetime(vent.pop('Timestamp'))

# tmp = vent.head(20)

print('tmp')