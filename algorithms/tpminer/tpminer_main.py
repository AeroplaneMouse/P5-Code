from logging2 import *
from tpmmodels.DB import DB
from tpmmodels.Ep_sup import Ep_sup
from tpmmodels.Endpoint import Endpoint
from tpmmodels.Projected_cs import Projected_cs
from algorithms.tpminer.TPSpan import TPSpan
from algorithms.tpminer.db_construct import db_construct
from algorithms.tpminer.tpminer import TDBToEndpointSequenceList


def tpminer_main(mdb, min_sup, logger):
    # Logging
    log = Log('Starting TPMiner', Severity.NOTICE)
    logger.log(log)

    TP = set()
    temp = TDBToEndpointSequenceList(mdb)
    validate_data(temp)

    log = Log('Converted to Endpoints', Severity.NOTICE)
    logger.log(log)

    db = convert_to_db(temp)
    n = len(db.ES)
    min_occ = n * min_sup

    FE = FindFE(db.ES, min_sup, min_occ, logger)

    log = Log("{} frequent endpoints discovered with {} min_sup".format(len(FE), min_sup), Severity.NOTICE)
    logger.log(log)

    i = 0
    j = len(FE)
    logger.log(ProgressLog('TPMiner:', progress=0))
    for s in FE:
        #db_s = db_construct(db, [s], [s])
        db_pruned, db_s = db_construct(db, s)

        #TPSpan([s], db_s, min_sup, TP, [s])
        log = Log("Calling tpspan with ep {} in {} client sequences".format(s, s.Support), Severity.INFO)
        logger.log(log)
        TPSpan([s], db_s, min_occ, TP, db_pruned, db)

        i += 1
        logger.log(ProgressLog('TPMiner:', progress=(i/j)))

    return TP


def FindFE(mdb, min_sup, min_occ, logger):
    FE = set()
    support_list = []

    for eps in mdb:
        support_list = acc_sup(eps.Ep_list, support_list)

    log = Log("{} unique endpoints found in database".format(len(support_list)), Severity.NOTICE)
    logger.log(log)
    for ep in support_list:
        if ep.Support >= min_occ:
            FE.add(ep)
    return FE


def acc_sup(eps, support_list):
    for ep in list(filter(lambda x: x.IsStart, eps)):
        for s in support_list:
            if s == ep:
                if not s.Counted:
                    s.Support = s.Support + 1
                    s.Counted = True
                break
        else:
            s_new = Endpoint(ep.Label, ep.IsStart, 0)
            s_new.Support = s_new.Support + 1
            s_new.Counted = True
            support_list.append(s_new)

    for s in support_list:
        s.Counted = False

    return support_list


def convert_to_db(mdb):
    temp = DB([])
    i = 0
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
                ep.Prune = True
                for epp in l[i:]:
                    if epp.Label == label and not epp.IsStart and not epp.Prune:
                        epp.Prune = True
                        break
            i += 1

    for l in data:
        for ep in l:
            if not ep.Prune:
                print("fail")
                print(l)
            ep.Prune = False

