class Endpoint:
    def __init__(self, label, isStart, parenthesis):
        self.Label = label
        self.OccurNum = 0
        self.IsStart = isStart
        self.Parenthesis = parenthesis
        self.Prune = False

    def __str__(self):
        return self.Label + ("+" if self.IsStart == True else '-')
        #return "true" if self.Prune else "false"

    def __repr__(self):
    	return self.__str__()
