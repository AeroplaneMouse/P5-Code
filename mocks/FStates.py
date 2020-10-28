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

F = FState(
    'F',
    pa.to_datetime('06:00:00'),
    pa.to_datetime('08:00:00'))

G = FState(
    'G',
    pa.to_datetime('06:00:00'),
    pa.to_datetime('07:00:00'))

H = FState(
    'H',
    pa.to_datetime('06:30:00'),
    pa.to_datetime('09:00:00'))

All = [A, B, C, F, G, H]
