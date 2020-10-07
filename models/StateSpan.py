class StateSpan:
    def __init__(self, clientID, state, startTime, endTime):
        self.ClientID = clientID
        self.State = state
        self.Start = startTime
        self.End = endTime

    def __str__(self):
        output = '{:>8} | {:>8} | {:>20} | {:>20}'.format(
            str(self.ClientID),
            str(self.State),
            str(self.Start),
            str(self.End)
        )
        return output