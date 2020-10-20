class FState:
    def __init__(self, state, start, end):
        self.State = state  # String
        self.Start = start  # String or pandas datetime
        self.End = end      # String or pandas datetime

    def __str__(self):
        return self.State

    def __repr__(self):
        return self.__str__()
