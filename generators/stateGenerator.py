class StateGenerator:
    # The last generated states
    LastStates = None

    def __init__(self, minValue, maxValue, increment):
        self.MinValue = minValue
        self.MaxValue = maxValue
        self.Increment = increment

    # Generates an dictionary with states between min and max
    # with increment as the space
    def GenerateStates(self):
        states = {}
        value = self.MinValue

        while value < self.MaxValue:
            # states[value] = State(value, value + INCREMENT)
            states[value] = str(value) + " -> " + str(value + self.Increment)
            value += self.Increment

        self.LastStates = states
        return states