import sqlite3
import csv

# State values
MIN_VALUE = -50
INCREMENT = 1
MAX_VALUE = 50

# Create states
def create_states():
    states = {}
    value = MIN_VALUE

    while value < MAX_VALUE:
        states[value] = str(value) + " -> " + str(value + INCREMENT)
        value += INCREMENT

    return states

# Maps a value to a state
def get_state(value, states):
    interval = MIN_VALUE

    while interval < value:
        interval += INCREMENT
    interval -= INCREMENT

    return states[interval]


# Removes dirt from timestamp
def clean_time(dirtyTime):
    return dirtyTime[:-8] + "00"


# Loads the file, converts sensor temperatur to states and saves every thing in the given database
def load_csv_to_db(filepath, conn):
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE ventData(time_slice TEXT, day TEXT, out_box TEXT, box_in TEXT, in_box TEXT, box_out TEXT);''')
    conn.commit()

    # Read file and insert data
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')
        counter = 0
        states = create_states()

        # [time] [day] [TimeStampCount] [BoxOut] [BoxIn] [InBox] [OutBox]  
        first = True
        for row in reader:
            # Skip first
            if first:
                first = False
            else:
                record = [
                    clean_time(row[0]), # Time
                    row[1].lower(),      # Day of week
                    get_state(float(row[6]), states), # OutBox
                    get_state(float(row[4]), states), # BoxIn
                    get_state(float(row[5]), states), # InBox
                    get_state(float(row[3]), states) # BoxOut
                ]

                # Insert
                #[Time] [OutBox] [BoxIn] [InBox] [BoxOut]
                c.execute('''INSERT INTO ventData VALUES(?,?,?,?,?,?);''', record)

                # Break
                counter += 1
                if counter > 30:
                    break

    conn.commit()

def addEntry(entry, cur):
    cur.execute('INSERT INTO temporal_vent VALUES(?,?,?,?);',
        entry['clientID'], 
        entry['state'], 
        entry['startTime'], 
        entry['endTime'])


def create_entry(id, table):
    entry = {
        'clientID': id,
        'state': table[2],
        'startTime': table[0],
        'endTime': table[0],
    }
    return entry

def create_temporal_table(conn):
    c = conn.cursor()

    c.execute('''
        CREATE TABLE temporal_vent(
            clientID INTEGER, 
            state TEXT, 
            startTime TEXT, 
            endTime TEXT
        );
    ''')
    conn.commit()


def convert_sensor_to_temporal(sensor, conn):
    c = conn.cursor()

    table = c.execute('''SELECT time_slice, day, ''' + sensor + ''' FROM ventData;''')
    conn.commit()

    currentDay = table[0][1]
    entry = create_entry(1, table[0])

    for t in table[1:]:
        time = t[0]
        day = t[1]
        state = t[2]

        # End current and start new
        if state != entry['state'] or day != currentDay:
            # Save current entry
            addEntry(entry)

            # Change entry
            entry = create_entry(entry['clientID'], t)
            
        # Update ID
        if day != currentDay:
            entry['clientID'] += 1

        # Update end time
        entry['endTime'] = time

    conn.commit()



def create_temporal_entries(conn):
    create_temporal_table(conn)

    sensors = ['out_box', 'box_in', 'in_box', 'box_out']
    for sensor in sensors:
        print(sensor)
        convert_sensor_to_temporal(sensor, conn)


    # create_entry(conn)
    



    return





conn = sqlite3.connect(':memory:')
load_csv_to_db('datasets/vent-minute.csv', conn)

create_temporal_entries(conn)

# Print database data
c = conn.cursor()
for row in c.execute('SELECT * FROM temporal_vent'):
    print(row)

conn.close()

