from PyQt5 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('imba_db.db3')
con.open()
if 'homelib' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec('''create table homelib(id integer primary key autoincrement, name text, secondname text, 
        otchestvo text, yearprint integer, publishing text, storage text, on_storage text, quarcode_add text,
        dateadd integer, dataprint integer ''')
    #id name, second_name, otchestvo, year_print, publishing, storage, on_storage, quarcode_add, date_add,
query = QtSql.QSqlQuery()
#query.prepare("insert into good values(null, :name, :count)")
#query.prepare(''' insert into home_lib values (name, second_name, otchestvo, year_print, publishing, storage
#    , on_storage, quarcode_add, date_add''')
#query.exec(''' insert into home_lib values ('Борис', 'Ермаков', 'Петрович', 1995, 'ЭКСПО', 'в шкафу',
#    'первый шкаф, вторая полка, второй ряд', 'нет куаркода', '03-06-2019' ''')
#lst1 = ['Бумага офисная', 'Фотобумага', 'Картридж']
#lst2 = [15, 8, 3]
#query.bindValue(':name', lst1)
#query.bindValue(':count', lst2)
#query.execBatch()
con.close()