class IndexSet:
    def __init__(self, pattern, indexRecords):
        self.Pattern = pattern
        self.Records = indexRecords

    def __str__(self):
        output = '{:>5} {:>80} {:>5}\n'.format('pos', 'Time range', 'CS')

        for r in self.Records:
            output += str(r)

        return output
