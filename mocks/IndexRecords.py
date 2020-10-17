from models.IndexRecord import IndexRecord
from models.Interval import Interval


A = IndexRecord(
    0,
    [Interval('2013-07-01 04:01:14', '2013-07-01 13:08:17')],
    0
)

B = IndexRecord(
    1,
    [Interval('2013-07-01 04:01:14', '2013-07-01 14:57:17')],
    0
)


All = [A, B]
