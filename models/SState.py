class SState:
    def __init__(self, stateName, appearsIn):
        self.StateName = stateName
        self.AppearsIn = appearsIn
        self.Support = None

    def __str__(self):
        return '{} | {:<10} | {:.2f}'.format(
            self.StateName,
            str(self.AppearsIn),
            self.Support
        )

    def __repr__(self):
        return self.__str__()
