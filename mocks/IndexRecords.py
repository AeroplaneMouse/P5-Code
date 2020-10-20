from models.IndexRecord import IndexRecord
from models.Interval import Interval


# 0_20->25
A0 = IndexRecord(
    0,
    [Interval('2013-07-01 04:01:14', '2013-07-01 13:08:17')],
    1
)
B0 = IndexRecord(
    0,
    [Interval('2013-07-02 07:58:29', '2013-07-02 08:00:29')],
    2
)
C0 = IndexRecord(
    0,
    [Interval('2013-07-03 00:00:28', '2013-07-03 04:24:26')],
    3
)


All = []
