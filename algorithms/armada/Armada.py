from algorithms.armada.MineIndexSet import MineIndexSet

class Armada:
    def __init__(self, cs, states):
        self.CS = cs
        self.States = states

    def Run(self, minSup):
        RemoveStates(minSup, self.States)

        for state in self.States:
            s = state.StateName

            # Create pattern

            # Create indexSet

            # Mine indexSet 


# Remove states that does not meet min support
def RemoveStates(minSup, states):
    for i in reversed(range(0, len(states))):
        if states[i].Support < minSup:
            del states[i]


