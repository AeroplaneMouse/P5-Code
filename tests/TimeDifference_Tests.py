import pandas as pa




#####################################################################
# Tests

print('********************')
print('Testing Pandas capabilities of combaring time')


print()
print('# Time addition')
A = pa.to_datetime('10:00')
B = pa.to_timedelta('01:00:00')
print('Adding time: {} + {}'.format(A, B))

result = A + B
if result == pa.to_datetime('11:00'):
    print('Result: {}'.format(result))
    print('Success')
else:
    print('Fail')



# print()
# print('# ')
