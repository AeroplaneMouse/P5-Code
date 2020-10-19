from models.IndexRecord import IndexRecord
from models.Interval import Interval

# 0_20->25
A = IndexRecord(
    0,
    [Interval('2013-07-01 04:01:14', '2013-07-01 13:08:17')],
    0
)

# 1_20->25
B = IndexRecord(
    1,
    [Interval('2013-07-01 04:01:14', '2013-07-01 14:57:17')],
    0
)

# 0_20->25
C = IndexRecord(
    0,
    [Interval('2013-07-01 13:09:17', '2013-07-01 13:10:17')],
    5,
)

All = [A, B, C]
