import copy as c
import testSuite as t
from tpmmodels.DB import DB
from mocks.Mini_database import *
from algorithms.tpminer.count_support import count_support
from tpmmodels.Projected_cs import Projected_cs


def test_count_support():
    #test with 5 equivalent cs of 5  starting endpoints. should add all endpoints to FE
    prfx = [a_s]
    Ep = [c_s_1, c_f_1, c_s_1, c_f_1, a_f_1]
    Ep2 = [c_s_1, c_f_1, c_s_1, c_f_1, a_f_1]
    Ep3 = [c_s_1, a_f_1]

    db = DB(prfx)
    cs = Projected_cs(prfx)
    cs.Ep_list = Ep
    cs2 = Projected_cs(prfx)
    cs2.Ep_list = Ep2
    cs3 = Projected_cs(prfx)
    cs3.Ep_list = Ep3

    db.ES = [cs, cs2, cs3]


    FE = count_support(db, 0.99)

    for e in FE:
        print(str(e.Label) + " " + str(e.IsStart) + " " + str(e.Parenthesis))
    #t.test(FE == expected_result, "count_support Test #1")


print('********************')
print('Testing count_support.py')
print()


test_count_support()
