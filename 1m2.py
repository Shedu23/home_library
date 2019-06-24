from PyQt5 import QtWidgets, QtSql
import sys

class MyWindow(QtWidgets.QWidget):
    def __inti__(self, parent=None):
        #QtWidgets.QWidget.__init__(self, parent)
        #self.resize(300, 100)
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QWidget()
        window.setWindowTitle("QRelationalSqlTableModel")
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('hl.db3')
        con.open()

        stm = QtSql.QSqlRelationalTableModel(parent=window)
        stm.setTable('good')
        stm.setSort(1, QtCore.Qt.AscendingOrder)
        # Задаем для поля категории связь с таблицей списка категорий
        stm.setRelation(3, QtSql.QSqlRelation('category', 'id', 'catname'))
        stm.select()
        stm.setHeaderData(1, QtCore.Qt.Horizontal, 'Название')
        stm.setHeaderData(2, QtCore.Qt.Horizontal, 'Кол-во')
        stm.setHeaderData(3, QtCore.Qt.Horizontal, 'Категория')
        vbox = QtWidgets.QVBoxLayout()
        tv = QtWidgets.QTableView()
        tv.setModel(stm)
        tv.hideColumn(0)
        tv.setColumnWidth(1, 150)
        tv.setColumnWidth(2, 60)
        tv.setColumnWidth(3, 150)
        vbox.addWidget(tv)
        btnAdd = QtWidgets.QPushButton("&Добавить запись")
        btnAdd.clicked.connect(addRecord)
        vbox.addWidget(btnAdd)
        btnDel = QtWidgets.QPushButton("&Удалить запись")
        btnDel.clicked.connect(delRecord)
        vbox.addWidget(btnDel)

    def addRecord():
        stm.insertRow(stm.rowCount())

    def delRecord():
        stm.removeRow(tv.currentIndex().row())
        stm.select()




if __name__ == "__main__":
    import sys
    #app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    #window.show()
    #sys.exit(app.exec_())
    window.setLayout(vbox)
    window.resize(420, 250)
    window.show()
    sys.exit(app.exec_())

#con.close()