import psycopg2
from pprint import pprint


class DatabaseConnection:
    """This class handles postgres DB"""

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database='stackover', user='postgres', host='localhost', password='keko', port='5432'
            )
            self.cursor = self.conn.cursor()
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

    def create_tables(self):

        """Create tables needed"""

        create_tables_command1 = """CREATE TABLE IF NOT EXISTS users(
             user_id SERIAL PRIMARY KEY,
             username VARCHAR(100),
             email VARCHAR(100) NOT NULL, 
             password VARCHAR(15) NOT NULL
         );"""

        create_tables_command2 = """CREATE TABLE IF NOT EXISTS questions(
             question_id SERIAL PRIMARY KEY,
             title VARCHAR(100),
             body VARCHAR(255) NOT NULL, 
             tag VARCHAR(50) NOT NULL
         );"""

        create_tables_command3 = """CREATE TABLE IF NOT EXISTS answers(
             answer_id SERIAL PRIMARY KEY,
             body VARCHAR(100)
         );"""
       
        try:
           self.cursor.execute(create_tables_command2)
           self.cursor.execute(create_tables_command3)
           self.cursor.execute(create_tables_command1)
        except:
             pprint('Cant connect to the database')


conn = DatabaseConnection()
conn.create_tables()
