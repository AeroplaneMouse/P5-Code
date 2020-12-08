from logging import *
from tpmmodels.DB import DB
from tpmmodels.Ep_sup import Ep_sup
from tpmmodels.Endpoint import Endpoint
from algorithms.tpminer.TPSpan import TPSpan
from tpmmodels.Projected_cs import Projected_cs
from algorithms.tpminer.db_construct import db_construct
from algorithms.tpminer.tpminer import TDBToEndpointSequenceList


def tpminer_main(mdb, min_sup, logger):
    # Logging
    log = Log('Starting TPMiner', Severity.NOTICE)
    logger.log(log)

    TP = set()
    temp = TDBToEndpointSequenceList(mdb)

    log = Log('Converted to Endpoints', Severity.NOTICE)
    logger.log(log)


    db = convert_to_db(temp)

    FE = FindFE(db.ES, min_sup)

    i = 1
    n = len(FE)

    for s in FE:
        #db_s = db_construct(db, [s], [s])
        db_pruned, db_s = db_construct(db, [s])

        #TPSpan([s], db_s, min_sup, TP, [s])
        TPSpan([s], db_s, min_sup, TP, db_pruned)

        m = 'TPMiner {:0.1f}%'.format((i/n)*100)
        log = Log(m, Severity.INFO)
        logger.log(log)

        i += 1

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
    i = 1
    for l in mdb:
        cs = Projected_cs([])
        cs.Ep_list = l
        cs.cs_id = i
        temp.ES.append(cs)
        i += 1

    return temp

def validate_data(data):
    for l in data:
        i = 1
        for ep in l:
            if ep.IsStart:
                label = ep.Label
                ep.Foo = True
                for epp in l[i:]:
                    if epp.Label == label and not epp.IsStart and not epp.Foo:
                        epp.Foo = True
                        break
            i += 1

    for l in data:
        for ep in l:
            if not ep.Foo:
                print("fail")
                print(l)

