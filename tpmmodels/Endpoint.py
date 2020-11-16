class Endpoint:
    def __init__(self, label, isStart, parentes):
        self.Label = label
        self.OccurNum = 0 
        self.IsStart = isStart
        self.Parentes = parentes

    def __str__(self):
        return self.Label