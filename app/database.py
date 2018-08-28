import psycopg2
import os

from pprint import pprint


class DatabaseConnection():
    """This class handles postres DB"""

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost", database="stackover", user="postgres", password=" "
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print('Connection successful')
        except (Exception, psycopg2.DatabaseError) as e:
            pprint(e, "Cannot connect to the database ")

    def close_db_connection(self):
        ''' closes connection to a database '''
        print('committing changes to db')
        self.conn.commit()
        print('db connection closed ')
        self.cursor.close()
        self.conn.close()