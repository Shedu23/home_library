from PyQt5 import QtCore, QtWidgets, QtSql
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle("Моя библиотека")
# Устанавливаем соединение с базой данных
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('hl.db3')
con.open()
# Создаем модель
sqm = QtSql.QSqlQueryModel(parent=window)
sqm.setQuery('select * from library order by author_secondname')
# Задаем заголовки для столбцов модели
sqm.setHeaderData(1, QtCore.Qt.Horizontal, 'Имя')
sqm.setHeaderData(2, QtCore.Qt.Horizontal, 'Фамилия')
sqm.setHeaderData(3, QtCore.Qt.Horizontal, 'Отчество')
sqm.setHeaderData(4, QtCore.Qt.Horizontal, 'Название книги')
sqm.setHeaderData(5, QtCore.Qt.Horizontal, 'Год издания')
sqm.setHeaderData(6, QtCore.Qt.Horizontal, 'Издательство')
sqm.setHeaderData(7, QtCore.Qt.Horizontal, 'Место в библиотеке')
sqm.setHeaderData(8, QtCore.Qt.Horizontal, 'На месте ли книги')
sqm.setHeaderData(9, QtCore.Qt.Horizontal, 'QR')
sqm.setHeaderData(10, QtCore.Qt.Horizontal, 'Дата добавления')
# Задаем для таблицы только что созданную модель
window.setModel(sqm)
# Скрываем первый столбец, в котором выводится идентификатор
window.hideColumn(0)
window.setColumnWidth(1, 150)
window.setColumnWidth(2, 150)
window.setColumnWidth(3, 150)
window.setColumnWidth(4, 600)
window.setColumnWidth(5, 100)
window.setColumnWidth(6, 100)
window.setColumnWidth(7, 250)
window.setColumnWidth(8, 100)
window.setColumnWidth(9, 150)
window.setColumnWidth(10, 100)
window.resize(1900, 760)
window.show()
sys.exit(app.exec_())