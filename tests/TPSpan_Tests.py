import testSuite as t
from mocks.Testing_DB import *
from algorithms.tpminer.TPSpan import TPSpan

def test_TPSpan():
    FE = {a_s, b_s, c_s}
    TP = set()
    l = [[a_s, b_s, b_f, a_f], 
                    [a_s, b_s, b_f, a_f, c_s, c_f], 
                    [b_s, b_f],
                    [b_s, b_f, c_s, c_f],
                    [c_s, c_f]]
    
    expected_result = set(tuple(i) for i in l)
    TPSpan([a_s], db, 0.5, TP, FE)
    t.test(TP == expected_result, 'TPSpan Test #1')

test_TPSpan()