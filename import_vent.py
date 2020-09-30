import sqlite3
import psycopg2 as postgres
import csv

from connect import connectDB, closeDB



STATE_ITEMS = {
    1: "A_",
    2: "B_",
    3: "C_",
    4: "D_"
}


def LoadData(fileName):
    # Read file
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            print(', '.join(row))

# States
def GetState(item, strValue):
    value = float(strValue)

    # Select prefix
    output = STATE_ITEMS.get(item, "ERROR")

    # Calculate postfix
    minValue = -50.0
    increment = 0.5
    counter = 0
    
    while value > minValue:
        counter += 1
        minValue += increment

    # Append postfix
    output += hex(counter)
    return output


def ImportCsvToDatabase(file, conn):
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE ventData(time_slice text, out_box text, box_in text, in_box text, box_out text)''')
    conn.commit()

    # Read file and insert data
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')
        counter = 0

        # [time] [day] [TimeStampCount] [BoxOut] [BoxIn] [InBox] [OutBox]  
        first = True
        for row in reader:
            if first:
                first = False
            else:
                record = [
                    row[0], # Time
                    GetState(1, row[6]), # OutBox
                    GetState(2, row[4]), # BoxIn
                    GetState(3, row[5]), # InBox
                    GetState(4, row[3])  # BoxOut
                ]

                # Insert
                #[Time] [OutBox] [BoxIn] [InBox] [BoxOut]
                c.execute('''INSERT INTO ventData VALUES(?,?,?,?,?)''', record)

                # Break
                counter += 1
                if counter > 30:
                    break

    result = conn.commit()
    print("Data insert: " + str(result))


def ImportDatabase(conn):
    c = conn.cursor()

    for row in c.execute('''SELECT * FROM ventData'''):
        print(row)




#conn = connectDB()



LoadData('datasets/vent-minute.csv')



#closeDB(conn)

#conn = sqlite3.connect(':memory:')

# ImportCsvToDatabase("Vent-minute.csv", conn)

# ImportDatabase(conn)
# conn.close()



# # Opens csv file (replace directory)
# with open('P5-Code/Weather.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter = ',')
#     for row in reader:
#         print(', '.join(row))

# # Creates database and empty table
# conn = sqlite3.connect(':memory:')

# cursor = conn.cursor()

# command_1 = """CREATE TABLE IF NOT EXISTS

# """

