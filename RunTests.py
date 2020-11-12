import sys

# Run all tests
if len(sys.argv) == 1:
    print('Running all tests')
    from tests import FindRelation_Tests
    from tests import CreatePattern_Tests
    from tests import CreateIndexSet_Tests
    from tests import MineIndexSet_Tests
    from tests import TimeDifference_Tests
    from tests import GetFirstEndTime_Tests
    from tests import Load_Tests
    from tests import fictionalData_Tests

# Run specific test
else:
    fileName = sys.argv[1]

    if fileName == 'CreatePattern_Tests' or fileName == 'CreatePattern':
        from tests import CreatePattern_Tests
    elif fileName == 'CreateIndexSet_Tests' or fileName == 'CreateIndex':
        from tests import CreateIndexSet_Tests
    elif fileName == 'MineIndexSet_Tests' or fileName == 'MineIndexSet':
        from tests import MineIndexSet_Tests
    elif fileName == 'TimeDifference_Tests' or fileName == 'TimeDifference':
        from tests import TimeDifference_Tests
    elif fileName == 'GetFirstEndTime_Tests' or fileName == 'GetFirstEndTime':
        from tests import GetFirstEndTime_Tests
    elif fileName == 'Load_Tests' or fileName == 'Load':
        from tests import Load_Tests
    elif fileName == 'fictionalData_Tests' or fileName == 'fictionalData':
        from tests import fictionalData_Tests

    # elif fileName == '#FileNameForTest_Tests#' or fileName == '#FileNameForTest#':
        # Put import stuff here
    else:
        print('Unknown test: \'{}\''.format(fileName))
