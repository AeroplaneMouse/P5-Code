from algorithms.armada.MineIndexSet import GetFirstEndTime
from mocks import Patterns
import pandas as pa

#####################################################################
# Setup



#####################################################################
# Tests

print('********************')
print('Testing GetFirstEndTime')


time = GetFirstEndTime(Patterns.C)

if time == pa.to_datetime('07:00:00'):
    print('Success')
else:
    print('Fail')
