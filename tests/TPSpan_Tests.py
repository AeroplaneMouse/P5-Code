import testSuite as t
from algorithms.tpminer.TPSpan import TPSpan
from mocks.Mini_database import *
from tpmmodels.Projected_cs import Projected_cs
from tpmmodels.DB import DB
from algorithms.tpminer.db_construct import db_construct

def test_TPSpan():
    TP = set()

    Ep = [b_f, c_s_1, c_f_1]
    Ep2 = [b_f, c_s_1, c_f_1]
    Ep3 = [b_f, c_s_1, c_f_1]

    cs = Projected_cs([b_s])
    cs.Ep_list = Ep
    cs2 = Projected_cs([b_s])
    cs2.Ep_list = Ep2
    cs3 = Projected_cs([b_s])
    cs3.Ep_list = Ep3

    db = DB([b_s])
    db.ES = [cs, cs2, cs3]

    TPSpan([b_s], db, 1, TP)

    for pattern in TP:
        print(pattern)

    expected_result = {(b_s, b_f, f_s, f_f),(b_s, b_f, c_s, c_f), (b_s, b_f), (b_s, b_f, c_s, f_s, f_f, c_f)}



    t.test(TP == expected_result, 'TPSpan Test #1')

test_TPSpan()