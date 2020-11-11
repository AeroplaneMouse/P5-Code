import fictionalData as fic
import pandas as pa


def test(bool, message):
    if bool:
        print('[Success] ' + message)
    else:
        print('[Failed]  ' + message)


def testPeriods():
    start = pa.to_datetime('07:55')
    end = pa.to_datetime('12:00')

    startS = pa.to_datetime('14:00')
    endS = pa.to_datetime('15:00')

    sen = fic.Sensor('Test', range(1, 5), [fic.Period(start, end), fic.Period(startS, endS)])
    time = pa.to_datetime('01-01-2020 10:00')

    # Inside
    m = 'Check if time inside period: Return TRUE'
    test(sen.inPeriods(time), m)

    # Outside below
    time = pa.to_datetime('01-01-2020 07:54')
    m = 'Check if time outside below period: Return FALSE'
    test(not sen.inPeriods(time), m)

    # Outside above
    time = pa.to_datetime('01-01-2020 12:01')
    m = 'Check if time outside above period: Return FALSE'
    test(not sen.inPeriods(time), m)
    print()


def testSensorGetState():
    start = pa.to_datetime('07:55')
    end = pa.to_datetime('12:00')

    sen = fic.Sensor('Test', range(1, 5), [fic.Period(start, end)])

    # A wednesday
    time = pa.to_datetime('11-11-2020 10:00')
    m = 'Check Sensor getState in activeDay(middle): Return \'ON\''
    test(sen.getState(time) == 'ON', m)

    # A saturday
    time = pa.to_datetime('14-11-2020 10:00')
    m = 'Check Sensor getState outside activeDay(after falling edge): Return \'OFF\''
    test(sen.getState(time) == 'OFF', m)

    # A sunday
    time = pa.to_datetime('15-11-2020 10:00')
    m = 'Check Sensor getState outside activeDay(before raising edge): Return \'OFF\''
    test(sen.getState(time) == 'OFF', m)

    # A monday
    time = pa.to_datetime('17-11-2020 10:00')
    m = 'Check Sensor getState in activeDay(after raising edge): Return \'ON\''
    test(sen.getState(time) == 'ON', m)
    print()


print('********************')
print('Testing fictionalData')
print()

testPeriods()
testSensorGetState()
