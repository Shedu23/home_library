import psycopg2
from pprint import pprint

class DatabasConnector:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='Own_library' user='postgres' host='localhost' password='123!qwe' port='5433' "
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connec to to database")

    #def crete_table(self):

DatabasConnector()
database_connection.isert_new_record()


#https://www.youtube.com/watch?v=Z9txOWCWMwA