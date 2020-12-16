class Endpoint:
    def __init__(self, label, isStart, parenthesis):
        self.Label = label
        self.OccurNum = 0
        self.IsStart = isStart
        self.Parenthesis = parenthesis
        self.Prune = False
        self.In_paren = False

        self.Support = 0
        self.Counted = False

        #debugging
        self.Stop_pos = None
        self.Ep_list = None

    def __str__(self):
        #return "true" if self.Prune else "false"
        return str(self.Label) + str("+" if self.IsStart else '-')

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.Label, self.IsStart, self.In_paren))

    def __eq__(self, other):
        return (
            self.Label == other.Label
            and self.IsStart == other.IsStart
        )
