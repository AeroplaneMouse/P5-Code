import copy as c
import testSuite as t
from tpmmodels.DB import DB
from mocks.Mini_database import *
from algorithms.tpminer.count_support import count_support


def test_count_support():
    #test with 5 equivalent cs of 5  starting endpoints. should add all endpoints to FE
    prfx = []
    cs = [a_s, b_s, c_s, d_s, e_s]
    db = DB(prfx)
    db.ES = [cs, c.copy(cs), c.copy(cs), c.copy(cs), c.copy(cs)]

    FE = count_support(db, 0.99)

    expected_result = set(cs)
    print(expected_result)
    t.test(FE == expected_result, "count_support Test #1")


print('********************')
print('Testing count_support.py')
print()


test_count_support()
