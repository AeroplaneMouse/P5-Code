from algorithms.tpminer.tpminer import TDBToEndpointSequenceList
from tpmmodels.Ep_sup import Ep_sup
from algorithms.tpminer.db_construct import db_construct
from algorithms.tpminer.TPSpan import TPSpan
from tpmmodels.Endpoint import Endpoint
from tpmmodels.DB import DB
from tpmmodels.Projected_cs import Projected_cs

def tpminer_main(mdb, min_sup):
    TP = set()
    temp = TDBToEndpointSequenceList(mdb)
    print(mdb[0])

    #for ep in temp[0]:
        #print(ep)

    db = convert_to_db(temp)

    FE = FindFE(db.ES, min_sup)

    #for s in FE:
        #db_s = db_construct(db, [s])
        #TPSpan([s], db_s, min_sup, TP)

    return TP


def FindFE(mdb, min_sup):
    FE = set()
    suppList = []

    mdb_len = len(mdb)

    for cs in mdb:
        for ep in cs.Ep_list:
            if ep.IsStart:
                i = find_in_supp_list(ep, suppList)
                if i is not None:
                    suppList[i].Support += 1
                    suppList[i].Has_been_counted = True
                else:
                    suppList.append(Ep_sup(ep.Label, ep.IsStart, 1, 0))

        for e in suppList:
            e.Has_been_counted = False

    for e in suppList:
        if e.Support / mdb_len >= min_sup:
            FE.add(Endpoint(e.Label, e.IsStart, 0))

    return FE



def find_in_supp_list(ep, suppList):
    for i in range(len(suppList)):
        if ep.Label == suppList[i].Label and ep.IsStart == suppList[i].IsStart:
            return i

    return None


def convert_to_db(mdb):
    temp = DB([])

    for l in mdb:
        cs = Projected_cs([])
        cs.Ep_list = l
        temp.ES.append(cs)

    return temp