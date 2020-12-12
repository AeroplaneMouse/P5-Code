class Endpoint:
    def __init__(self, label, isStart, time):
        self.Time = time
        self.Label = label
        self.OccurNum = 0
        self.IsStart = isStart
        self.Prune = False

        self.Support = 0
        self.Counted = False

    def __str__(self):
        #return "true" if self.Prune else "false"
        return str(self.Label) + str("+" if self.IsStart else '-') + str(self.Time)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.Label, self.IsStart))

    def __eq__(self, other):
        return (
            self.Label == other.Label
            and self.IsStart == other.IsStart
        )
