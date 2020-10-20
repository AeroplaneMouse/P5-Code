import sys

# Run all tests
if len(sys.argv) == 1:
    print('Running all tests')
    from tests import CreatePattern_Tests

# Run specific test
else:
    test = sys.argv[1]

    if test == 'CreatePattern':
        from tests import CreatePattern_Tests
    elif test == '?':
        # Another test
        print()
    else:
        print('Unknown test: \'{}\''.format(test))
