class Endpoint:
    def __init__(self, label, isStart, parenthesis):
        self.Label = label
        self.OccurNum = 0
        self.IsStart = isStart
        self.Parenthesis = parenthesis
        self.Prune = False

    def __str__(self):
        #return "true" if self.Prune else "false"
        return str(self.Label) + str("+" if self.IsStart else '-') + str(self.parenthesis)

    def __repr__(self):
    	return self.__str__()

    def __hash__(self):
        return hash(self.Label)

    def __eq__(self, other):
        return (
            self.Label == other.Label
            and self.IsStart == other.IsStart
        )
