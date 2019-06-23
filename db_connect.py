# -*- coding: utf-8 -*-

import psycopg2
from pprint import pprint

class DatabasConnector:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='Own_library' user='postgres' host='localhost' password='123!qwe' port='5433'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except:
            print("Cannot connect to to database")

    def create_table(self):
        #create_table_command = "CREATE TABLE pet(id integer, name varchar(100), age integer NOT NULL)"
        create_table_command = '''
                                    CREATE TABLE home_books(
                                name	varchar(60),
                                second_name	varchar(60),
                                otchestvo	varchar(60),
                                year_print	int,
                                publishing	varchar(60),
                                storage		varchar(100), 
                                on_storage	varchar(40),
                                quarcode_add	varchar(40),
                                date_add	varchar(40),
                                id	int);

        '''

        print("Inicialization ... Create table")
        self.cursor.execute(create_table_command)

    def drop_table(self):
        try:
            create_table_command = "DROP TABLE home_books"
            self.cursor.execute(create_table_command)
        except:
            print("ОШИБКА:  таблица pet не существует")

    def insert_data_to_table(self):
        name = ["Борис", "Петров"]
        #create_table_command1 = u"Insert INTO home_books (name, second_name) VALUES ('"+name[0]+"','"+name[1]+"')"
        create_table_command = u'''
                                INSERT INTO home_books (name, second_name, otchestvo, year_print, publishing, storage,
                                 on_storage,quarcode_add, date_add, id)
                                VALUES ('Борис', 'Ермаков', 'Петрович', 1995, 'ЭКСПО', 'в шкафу',
                                 'первый шкаф, вторая полка, второй ряд', 'нет куаркода', '03-06-2019', 1);
        '''
        self.cursor.execute(create_table_command)

    def seach_data_in_table(self):
        self.cursor.execute("SELECT * FROM home_books")
        data = self.cursor.fetchall()
        for i in data:
            print(i)

if __name__== '__main__':
    database_connection = DatabasConnector()
    #database_connection.drop_table()
    #database_connection.create_table()
    #database_connection.drop_table()
    #database_connection.insert_data_to_table()
    database_connection.seach_data_in_table()


#https://www.youtube.com/watch?v=Z9txOWCWMwA



#INSERT INTO home_books (name, second_name, otchestvo, year_print, publishing, storage, on_storage,quarcode_add, date_add, id)
# VALUES ('Борис', 'Ермаков', 'Петрович', 1995, 'ЭКСПО', 'в шкафу', 'первый шкаф, вторая полка, второй ряд', 'нет куаркода', '03-06-2019', 1);


#INSERT INTO home_books (name, second_name, otchestvo, year_print, publishing, storage, on_storage,quarcode_add, date_add, id)
 #VALUES ('Борис', 'Алексеев', 'Алексеевич', 1995, 'ЭКСПО', 'в шкафу', 'первый шкаф, вторая полка, второй ряд', 'нет куаркода', '03-08-2017', 3);
#