import testSuite as t
from mocks.Mini_database import *
from algorithms.tpminer.point_pruning import point_pruning


def test_point_pruning():
    #test with prefix of length 1
    FE = {a_f, b_f, c_s, c_f, d_s, d_f}
    expected_return = {a_f, c_s, d_s}
    prfx = [a_s, a_f, a_s]

    t.test(point_pruning(FE, prfx) == expected_return, 'PointPruning Test #1')

    #Test on prefix with length 1
    FE = {a_s, a_f, b_f, c_s, c_f, d_s, d_f}
    expected_return = {a_s, a_f, c_s, c_f, d_s}
    prfx = [a_s, c_s]

    t.test(point_pruning(FE, prfx) == expected_return, 'PointPruning Test #2')


print('********************')
print('Testing PointPruning')
print()

test_point_pruning()
