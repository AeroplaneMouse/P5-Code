import testSuite as t
import mocks.FStates as states
from algorithms.armada.FindRelation import FindRelation


def TestFindRelation():
    result = (
        FindRelation(states.A, states.B) != 'c'
        or FindRelation(states.A, states.C) != 'f'
        or FindRelation(states.B, states.C) != 'o'
        or FindRelation(states.B, states.A) != 'X'
    )

    t.test(not result, 'FindRelation_Tests')


TestFindRelation()
