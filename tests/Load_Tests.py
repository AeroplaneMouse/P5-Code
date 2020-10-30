from preprocessors.Load import LoadPreprocessor

PATH = '../Datasets/Load-minute.csv'

load = LoadPreprocessor(PATH, ',')

load.GenerateTemporalMdb()
