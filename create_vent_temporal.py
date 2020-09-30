import sqlite3
import csv

# State values
MIN_VALUE = -50
INCREMENT = 5
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
    c.execute('''CREATE TABLE ventData(time_slice text, out_box text, box_in text, in_box text, box_out text)''')
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
                    get_state(float(row[6]), states), # OutBox
                    get_state(float(row[4]), states), # BoxIn
                    get_state(float(row[5]), states), # InBox
                    get_state(float(row[3]), states) # BoxOut
                ]

                # Insert
                #[Time] [OutBox] [BoxIn] [InBox] [BoxOut]
                c.execute('''INSERT INTO ventData VALUES(?,?,?,?,?)''', record)

                # Break
                counter += 1
                if counter > 30:
                    break

    conn.commit()

def create_temporal_entries(conn):
    create_temporal_table('', conn)

    create_entry(conn)
    



    return


conn = sqlite3.connect(':memory:')
load_csv_to_db('datasets/vent-minute.csv', conn)

# Print database data
c = conn.cursor()
for row in c.execute('SELECT * FROM ventData'):
    print(row)

conn.close()

