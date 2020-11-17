

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


# Print the last 'n' patterns
def PrintNPatterns(n, patterns):
    print('Last {} patterns:'.format(n))
    i = len(patterns) - n - 1
    for p in patterns[-n:]:
        print(i)
        print(p)
        print()
        i += 1


def PrintResults(minSupport, maxGap, patterns, skippedDays, frequentStates, path):
    # Remove extension and dataset folder
    path = path[9:-4]

    print('########################################')
    print('# Dataset: {:>29}'.format(path))
    print('# Minimum support: {:>21}'.format(minSupport))
    print('# Maximum gap: {:>25}'.format(str(maxGap)))
    print('# Patterns found: {:>22}'.format(len(patterns)))
    print('# Skipped days: {:>24}'.format(len(skippedDays)))
    print('# Frequent states: {:>21}'.format(len(frequentStates)))


def PrintPatternCount(count):
    print('#')
    for key in count:
        print('# {:>2}-patterns: {:>25}'.format(
            key,
            count[key]))
