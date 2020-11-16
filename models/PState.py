class PState:
    def __init__(self, interval):
        self.Interval = interval
        self.AppearsIn = []

    def __str__(self):
        return '{} | {}'.format(self.Interval, self.AppearsIn)

    def __repr__(self):
        return self.__str__()
