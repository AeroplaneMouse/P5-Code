from preprocessors.vent import VentPreprocessor
from algorithms.armada.MineIndexSet import MineIndexSet, ComputePotentialStems
from mocks import IndexSets
from algorithms.armada import Storage
import pandas as pa


# Preprocessing
vent = VentPreprocessor()
vent.InitializeDataFrame('datasets/vent-minute-short.csv', ';')
cs = vent.GenerateTemporalDataFrame()


# Insert MDB into storage and split into multiple cs DataFrames
Storage.MDB = []
clientID = 0
data = {'ClientID': [], 'State': [], 'Start': [], 'End': []}
for i in range(0, len(cs)):
    singleCS = cs.iloc[i]

    # Change cs
    if clientID != singleCS.ClientID or i == len(cs)-1:
        Storage.MDB.append(pa.DataFrame(data))

        # Reset
        clientID = singleCS.ClientID
        data = {'ClientID': [], 'State': [], 'Start': [], 'End': []}

    data['ClientID'].append(singleCS.ClientID)
    data['State'].append(singleCS.State)
    data['Start'].append(singleCS.Start)
    data['End'].append(singleCS.End)

# for i in range(0, len(data['ClientID'])):
#     print('{} | {} | {} | {}'.format(
#         data['ClientID'][i],
#         data['State'][i],
#         data['Start'][i]
#         data['End'][i]))

# print(len(Storage.MDB))
# print(Storage.MDB)


print('********************')
print('Testing ComputePotentialStems')
print()


stems = ComputePotentialStems(indexSet=IndexSets.A, frequentStates=None, minSup=0.7)

print()
print('New stems:')
print(stems)
