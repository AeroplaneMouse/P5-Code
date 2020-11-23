import sys

# Run all tests
if len(sys.argv) == 1:
    print('#'*30)
    print('{:<29}#'.format('# Running all tests'))
    print('#'*30)
    print()

    from tests import FindRelation_Tests
    print()
    from tests import CreatePattern_Tests
    print()
    from tests import CreateIndexSet_Tests
    print()
    from tests import MineIndexSet_Tests
    print()
    from tests import Load_Tests
    print()
    from tests import fictionalData_Tests
    print()
    from tests import db_construct_Tests
    print()
    from tests import point_pruning_Tests
    print()
    from tests import TDB_to_endpoint_Tests
    print()
    from tests import count_support_Tests


# Run specific test
else:
    fileName = sys.argv[1]

    if fileName == 'FindRelation_Tests' or fileName == 'FindRelation':
        from tests import FindRelation_Tests

    elif fileName == 'CreatePattern_Tests' or fileName == 'CreatePattern':
        from tests import CreatePattern_Tests

    elif fileName == 'CreateIndexSet_Tests' or fileName == 'CreateIndex':
        from tests import CreateIndexSet_Tests

    elif fileName == 'MineIndexSet_Tests' or fileName == 'MineIndexSet':
        from tests import MineIndexSet_Tests

    elif fileName == 'Load_Tests' or fileName == 'Load':
        from tests import Load_Tests

    elif fileName == 'fictionalData_Tests' or fileName == 'fictionalData':
        from tests import fictionalData_Tests

    elif fileName == 'db_construct_Tests' or fileName == 'db_construct':
        from tests import db_construct_Tests

    elif fileName == 'point_pruning_Tests' or fileName == 'point_pruning':
        from tests import point_pruning_Tests

    elif fileName == 'TDB_to_endpoint_Tests' or fileName == 'TDB_to_endpoint':
        from tests import TDB_to_endpoint_Tests
    elif fileName == 'count_support_Tests' or fileName == 'count_support':
        from tests import count_support_Tests


    # elif fileName == '#FileNameForTest_Tests#' or fileName == '#FileNameForTest#':
        # Put import stuff here
    else:
        print('Unknown test: \'{}\''.format(fileName))
