class State:
    def __init__(self, minValue, maxValue):
        self.MinValue = minValue
        self.MaxValue = maxValue

    def __str__(self):
        return str(self.MinValue) + ' -> ' + str(self.MaxValue)