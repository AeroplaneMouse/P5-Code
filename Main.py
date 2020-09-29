import sqlite3
import csv

# Opens csv file (replace directory)
with open('/Users/Andre/Documents/GitHub/P5-Code/Weather.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        print(', '.join(row))

# Creates database and empty table
conn = sqlite3.connect(':memory:')

cursor = conn.cursor()

command_1 = """CREATE TABLE IF NOT EXISTS

"""

