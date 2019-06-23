# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtSql

class MyWindow(QtWidgets.QWidget):
    mysignal = QtCore.pyqtSignal(int, int)
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Генерация сигнала из программы")
        self.resize(500, 400)
        self.button1 = QtWidgets.QPushButton("Нажми меня")
        self.button2 = QtWidgets.QPushButton("Кнопка 2")
        self.button3 = QtWidgets.QPushButton("Add data to DB")
        self.button4 = QtWidgets.QPushButton("Select * FROM DB")
        self.button5 = QtWidgets.QPushButton("EXIT")
        self.button6 = QtWidgets.QPushButton("QR code Generate")
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)
        vbox.addWidget(self.button5)
        vbox.addWidget(self.button6)
        self.setLayout(vbox)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.button3.clicked.connect(self.on_clicked_button3)
        self.button4.clicked.connect(self.on_clicked_button4)
        self.button5.clicked.connect(QtWidgets.qApp.quit)
        self.button6.clicked.connect(self.on_clicked_button6)
        self.mysignal.connect(self.on_mysignal)

    def on_clicked_button1(self):
        print("Нажата кнопка button1")
        # Генерируем сигналы
        self.button2.clicked[bool].emit(False)
        self.mysignal.emit(10, 20)

    def on_clicked_button2(self):
        print("Нажата кнопка button2")

    def on_clicked_button3(self):
        try:
            #app = QtWidgets.QApplication(sys.argv)
            con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            con.setDatabaseName('imba_db.db3')
            con.open()
            query = QtSql.QSqlQuery()
            query.prepare("insert into good values(null, :name, :count)")
            lst1 = ['Бумага офисная', 'Фотобумага', 'Картридж']
            lst2 = [15, 8, 3]
            query.bindValue(':name', lst1)
            query.bindValue(':count', lst2)
            query.execBatch()
            con.close()
        except:
            print("Cant add data to DB imba_db.db3")


        print("Data add to DB imba_db.db3")

    def on_clicked_button4(self):
        # Пока данная кнопка не работает
        try:
            #app = QtWidgets.QApplication(sys.argv)
            con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            con.setDatabaseName('imba_db.db3')
            con.open()
            query = QtSql.QSqlQuery()
            query.exec("select * from good order by goodname")
            lst = []
            print(lst)
            '''
                if query.isActive():
                query.first()
                while query.isValid():
                    lst.append(query.value('goodname') + ': ' +
                               str(query.value('goodcount')) + ' шт.')
                    query.next()
                for p in lst: print(p)
            con.close()
            '''

        except:
            print("Error to connect DB")

    def on_clicked_button6(self):
        import pyqrcode

        for i in range(1, 3):
            img_name = "The book number id is : " + str(i)
            print(img_name)
            img_name = img_name + '.svg'
            img = pyqrcode.create(img_name)
            img.svg(img_name, scale=4)

    def plus(self, a,b):
        c = a + b
        return c

    def on_mysignal(self, x, y):
        print("Обработан пользовательский сигнал mysignal()")
        print("x =", x, "y =", y)

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self,
                       "Подтверждение закрытия окна",
                       "Вы действительно хотите закрыть окно?",
                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                       QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)
        else:
            e.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())