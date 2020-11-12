from algorithms.armada.CreateIndexSet import CreateIndexSet
from algorithms.armada import Storage
from preprocessors.Vent import VentPreprocessor


print('********************')
print('Testing CreateIndexSet')
print()

PATH = 'datasets/vent-minute-shorter.csv'
preprocessor = VentPreprocessor(PATH, ';')

mdb = preprocessor.GenerateTemporalMdb(interval=5)