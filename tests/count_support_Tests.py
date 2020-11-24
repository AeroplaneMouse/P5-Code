from copy import copy
import testSuite as t
from tpmmodels.DB import DB
from mocks.Mini_database import *
from algorithms.tpminer.count_support import count_support


def test_count_support():
    prfx = [a_s, a_f]
    cs = [c_f, d_f, b_f]
    db = DB(prfx)
    db.ES = [cs, copy(cs), copy(cs), copy(cs), [c_f, a_f, b_f]]

    FE = count_support(db, 1)

    print(len(FE))


print('********************')
print('Testing count_support.py')
print()


test_count_support()
