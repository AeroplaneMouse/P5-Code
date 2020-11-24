import testSuite as t
from mocks.Testing_DB import *
from algorithms.tpminer.TPSpan import TPSpan

def test_TPSpan():
    FE = {a_s, b_s, c_s}
    expected_result = {[a_s, b_s, b_f, a_f], 
                    [a_s, b_s, b_f, a_f, c_s, c_f], 
                    [b_s, b_f],
                    [b_s, b_f, c_s, c_f],
                    [c_s, c_f]}

    TPSpan(a_s, d)