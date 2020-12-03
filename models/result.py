

class Result:
    patterns = None
    preprocessingTime = -1
    algorithmTime = -1
    frequentStates = None
    skippedDays = None
    dataset = ""
    minSupport = None
    maxGap = None

    def __init__(self, minSupport, maxGap, patterns, frequentStates):
        self.patterns = patterns
        self.frequentStates = []
        self.minSupport = minSupport
        self.maxGap = maxGap

    # Print the last 'n' patterns
    def printPatterns(self, n=-1):
        if n == -1 or n > len(self.patterns):
            n = len(self.patterns)

        print('Last {} patterns:'.format(n))
        i = len(self.patterns) - n - 1
        for p in self.patterns[-n:]:
            print(i)
            print(p)
            print()
            i += 1

    def print(self):
        # Remove extension and dataset folder
        dataset = self.dataset[9:-4]

        print('#'*42)
        print('# Dataset: {:>29} #'.format(dataset))
        print('# Minimum support: {:>21} #'.format(self.minSupport))
        print('# Maximum gap: {:>25} #'.format(str(self.maxGap)))
        print('# Patterns found: {:>22} #'.format(len(self.patterns)))
        print('# Skipped days: {:>24} #'.format(len(self.skippedDays)))
        print('# Frequent states: {:>21} #'.format(len(self.frequentStates)))
        print('# Preprocessing: {:>21.1f} s #'.format(self.preprocessingTime))
        print('# Algorithm time: {:>20.1f} s #'.format(self.algorithmTime))

        count = CountNPatterns(self.patterns)
        print('#' + ' '*40 + '#')
        for key in count:
            print('# {:>2}-patterns: {:>25} #'.format(
                key,
                count[key]))
        print('#'*42)


# Counts the number of different pattern types
def CountNPatterns(patterns):
    count = {}
    for p in patterns:
        pSize = len(p[0][1:])

        if pSize not in count:
            count[pSize] = 1
        else:
            count[pSize] += 1

    return count

def Test():
    a = Result(1, 2, 3, 4)

    a.algorithmTime