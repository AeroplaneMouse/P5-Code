import sys

# Run all tests
if len(sys.argv) == 1:
    print('Running all tests')
    from tests import CreatePattern_Tests

# Run specific test
else:
    fileName = sys.argv[1]

    if fileName == 'CreatePattern_Tests':
        from tests import CreatePattern_Tests
    elif fileName == 'CreateIndexSet_Tests':
        from tests import CreateIndexSet_Tests
    # elif fileName == '#FileNameForTestFile#':
        # Put import stuff here
    else:
        print('Unknown test: \'{}\''.format(fileName))
