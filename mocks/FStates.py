from models.FState import FState
import pandas as pa


A = FState(
    'A',
    7,
    22)

B = FState(
    'B',
    8,
    15)

C = FState(
    'C',
    10,
    22)

D = FState(
    '0_20->25',
    pa.to_datetime('2013-07-01 04:01:14'),
    pa.to_datetime('2013-07-01 13:08:17'))

E = FState(
    '1_20->25',
    pa.to_datetime('2013-07-01 04:01:14'),
    pa.to_datetime('2013-07-01 14:57:17'))

All = [A, B, C]
