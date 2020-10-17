class IndexRecord:
    def __init__(self, pos, intervals, ref):
        self.Pos = pos
        self.Intervals = intervals
        self.Ref = ref

    def __str__(self):
        return '{:>5} {:>80} {:>5}'.format(
            self.Pos,
            str(self.Interval),
            self.Ref)

    def __repr__(self):
        return self.__str__()