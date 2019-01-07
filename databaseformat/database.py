# # from os import environ
# import psycopg2
# from psycopg2.extras import RealDictCursor
# # import psycopg2
# # import psycopg2.extras
# # import os


# # class DatabaseConnection:
# #     def __init__(self):
# #         if os.getenv('APP_SETTINGS') == 'test_db':
# #             self.db = 'test_db'
# #         else:
# #             self.db = 'dcqtq6lt2rch47'

# #         # connection = psycopg2.connect(dbname=self.db, user='phillip', password='password123', host='localhost', port='5432')
# #         connection = psycopg2.connect(dbname=self.db, user='rzkfzvouaginmd',
# #                                       password='80d4f31f92593efe13bf6d5a51fc84b27d98e28478e877b16c5dadc637501205',
# #                                       host='ec2-54-221-207-184.compute-1.amazonaws.com', port='5432')
# #         connection.autocommit = True
# #         self.cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
# #         print(self.cursor)

# class Database:

#     def __init__(self):
#         """ create tables in the PostgreSQL database"""
#         commands = ( )
#         conn = None
#         try:
#             # read the connection parameters
#             params = config()
#             # connect to the PostgreSQL server
#             conn = psycopg2.connect(**params)
#             cur = conn.cursor()
#             # create table one by one
#             for command in commands:
#                 cur.execute(command)
#             # close communication with the PostgreSQL database server
#             cur.close()
#             # commit the changes
#             conn.commit()
#         except (Exception, psycopg2.DatabaseError) as error:
#             print(error)
#         finally:
#             if conn is not None:
#                 conn.close()


# if __name__ == "__main__":
#     db = Database()
#     db.create_tables()


import psycopg2
from config import config

def connect():
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
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()