from tpmmodels.DB import DB
from tpmmodels.Endpoint import Endpoint
from algorithms.tpminer import tpminer

def count_support(db_a, prefix, minSupport):

    FE = []
    start = bool
    end = bool



    for q in db_a:
        for ep in q:
            if not ep.IsStart:
                for i in q:
                    if i.label == ep.label:





            
