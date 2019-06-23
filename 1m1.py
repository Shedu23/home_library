from PyQt5 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('hl.db3')
con.open()

if 'library' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec('''create table library(id integer primary key autoincrement,
        author_name text, author_secondname text, author_otchestvo text, name_book, book_yearprint integer, 
        publishing text, locate_storage text, on_storage text, quarcode_add text, date_bookadd integer)''')

if 'library' in con.tables():
    query = QtSql.QSqlQuery()
    query.prepare('''insert into library values(null, :name, :sname, :fam, :nbook, :byear, :puble, :store, :here, :qr,
                  :thenadd)''')
    query.bindValue(':name', 'Александр')
    query.bindValue(':sname', 'Сергеевич')
    query.bindValue(':fam', 'Пушкин')
    query.bindValue(':nbook', 'Собрание сочиненеий. Том 4. Евгений. Онегин. Драматтические произведения')
    query.bindValue(':byear', 1960)
    query.bindValue(':puble', 'Государственное издательство художественной литературы')
    query.bindValue(':store', 'первая полка первый ряд')
    query.bindValue(':here', 'книгу читают')
    query.bindValue(':qr', 'нет куаркода')
    query.bindValue(':thenadd', 2019)
    query.exec_()

for i in con.tables():
    print(i)


con.close()