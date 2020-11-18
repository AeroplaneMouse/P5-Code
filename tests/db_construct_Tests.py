import testSuite as t
from mocks.Mini_database import *
from algorithms.tpminer.db_construct import db_construct

def test_db_construct():
    temp = db_construct(db, a_p)
    print(temp.ES)

    # t.test(boolean, 'Description')
    #        return '[Success] Description'

test_db_construct()
