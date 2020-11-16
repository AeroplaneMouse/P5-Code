class Endpoint:
    def __init__(self, label, isStart, parenthesis):
        self.Label = label
        self.OccurNum = 0 
        self.IsStart = isStart
        self.Parenthesis = parenthesis
        self.Prune = false


    def __str__(self):
        return self.Label