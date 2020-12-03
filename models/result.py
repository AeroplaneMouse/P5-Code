

class Result:
    patterns = None
    preprocessingTime = -1
    algorithmTime = -1
    frequentStates = None
    skippedDays = None
    dataset = ""
    minSupport = None
    maxGap = None
    errors = None

    def __init__(self, minSupport, maxGap, patterns=[], frequentStates=[], errors=[]):
        self.patterns = patterns
        self.frequentStates = frequentStates
        self.minSupport = minSupport
        self.maxGap = maxGap
        self.errors = errors

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
        out = '#'*42 + '\n'
        if len(self.errors) > 0:
            out += '# {:<38} #\n'.format('Errors:')
            for e in self.errors:
                out += '# {:<38} #\n'.format(e)
        else:
            # Remove extension and dataset folder
            dataset = self.dataset[9:-4]

            out +='# Dataset: {:>29} #\n'.format(dataset)
            out +='# Minimum support: {:>21} #\n'.format(self.minSupport)
            out +='# Maximum gap: {:>25} #\n'.format(str(self.maxGap))
            out +='# Patterns found: {:>22} #\n'.format(len(self.patterns))
            out +='# Skipped days: {:>24} #\n'.format(len(self.skippedDays))
            out +='# Frequent states: {:>21} #\n'.format(len(self.frequentStates))
            out +='# Preprocessing: {:>21.1f} s #\n'.format(self.preprocessingTime)
            out +='# Algorithm time: {:>20.1f} s #\n'.format(self.algorithmTime)

            count = CountNPatterns(self.patterns)
            out += '#' + ' '*40 + '#\n'
            for key in count:
                out += '# {:>2}-patterns: {:>25} #\n'.format(
                    key,
                    count[key])

        out += '#'*42 + '\n'
        print(out)


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