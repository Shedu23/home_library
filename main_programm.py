from PyQt5 import QtCore, QtWidgets, QtSql
import sys

def addRecord():
    # Вставляем пустую запись, в которую пользователь сможет
    # ввести нужные данные
    stm.insertRow(stm.rowCount())

def delRecord():
    # Удаляем запись из модели
    stm.removeRow(tv.currentIndex().row())
    # Выполняем повторное считывание данных в модель,
    # чтобы убрать пустую "мусорную" запись
    stm.select()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Моя библиотека")
# Устанавливаем соединение с базой данных
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('hl.db3')
con.open()
# Создаем модель
stm = QtSql.QSqlTableModel(parent=window)
stm.setTable('library')
stm.setSort(1, QtCore.Qt.AscendingOrder)
stm.select()
# Задаем заголовки для столбцов модели
#stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
#stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Кол-во')

stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Имя')
stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Фамилия')
stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Отчество')
stm.setHeaderData(4, QtCore.Qt.Horizontal, 'Название книги')
stm.setHeaderData(5, QtCore.Qt.Horizontal, 'Год издания')
stm.setHeaderData(6, QtCore.Qt.Horizontal, 'Издательство')
stm.setHeaderData(7, QtCore.Qt.Horizontal, 'Место в библиотеке')
stm.setHeaderData(8, QtCore.Qt.Horizontal, 'На месте ли книги')
stm.setHeaderData(9, QtCore.Qt.Horizontal, 'QR')
stm.setHeaderData(10, QtCore.Qt.Horizontal, 'Дата добавления')

# Задаем для таблицы только что созданную модель
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
# Скрываем первый столбец, в котором выводится идентификатор
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 150)
tv.setColumnWidth(3, 150)
tv.setColumnWidth(4, 600)
tv.setColumnWidth(5, 100)
tv.setColumnWidth(6, 100)
tv.setColumnWidth(7, 250)
tv.setColumnWidth(8, 100)
tv.setColumnWidth(9, 150)

vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("&Добавить запись")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Удалить запись")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(1900, 760)
window.show()
sys.exit(app.exec_())