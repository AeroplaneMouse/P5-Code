import psycopg2
from config import config

def connectDB():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return conn


def closeDB(conn):
    if conn is not None:
        conn.close()
        print('Database connection closed')
        return True
    else:
        print('No database connection')
        return False