class Interval:
    def __init__(self, start, end):
        self.Start = start
        self.End = end

    def __str__(self):
        return '[{}|{}]'.format(
            self.Start,
            self.End)

    def __repr__(self):
        return self.__str__()
