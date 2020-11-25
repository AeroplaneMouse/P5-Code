import testSuite as t
from mocks.Mini_database import *
from algorithms.tpminer.db_construct import db_construct
from tpmmodels.Projected_cs import Projected_cs
import copy


def test_db_construct():
    #two-pattern a_p, no pointsets, 3 equal client sequences
    Ep_list = [c_s, a_f, c_f, d_s, d_f]
    Ep_list2 = [c_s, a_f, c_f, d_s, d_f]
    Ep_list3 = [c_s, a_f, c_f, d_s, d_f]

    prfx = [a_s]

    cs = Projected_cs(prfx)
    cs.Ep_list = Ep_list
    cs2 = Projected_cs(prfx)
    cs2.Ep_list = Ep_list2
    cs3 = Projected_cs(prfx)
    cs3.Ep_list = Ep_list3

    cs_list = [cs, cs2, cs3]
    db = DB(prfx)
    db.ES = cs_list
    temp = db_construct(db, db.Pattern + [a_f]).ES
    result = []

    for proj_cs in temp:
        result.append(proj_cs.Ep_list)

    expected_result = [[d_s], [d_s], [d_s]]

    t.test(result == expected_result, 'Construct_db Test #1')

    #two-pattern a_p, a_p is pointset, result should be empty

    Ep_list = [c_s_1, a_f_1, c_f, d_s, d_f]
    Ep_list2 = [c_s_2, a_f_2, c_f, d_s, d_f]
    Ep_list3 = [c_s, a_f, c_f, d_s, d_f]

    prfx = [a_s_1]
    prfx2 = [a_s_2]
    prfx3 = [a_s_2]

    cs = Projected_cs(prfx)
    cs.Ep_list = Ep_list
    cs2 = Projected_cs(prfx2)
    cs2.Ep_list = Ep_list2
    cs3 = Projected_cs(prfx3)
    cs3.Ep_list = Ep_list3

    db.ES = [cs, cs2, cs3]

    db.Pattern = [a_s_1]

    temp = db_construct(db, db.Pattern + [a_f_1]).ES
    result = []
    for proj_cs in temp:
        result.append(proj_cs.Ep_list)
        print(proj_cs.Ep_list)




test_db_construct()
