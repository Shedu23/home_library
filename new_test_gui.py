# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
#import db_connect

class Ui_Form(object):

    def loadData(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='Own_library' user='postgres' host='localhost' password='123!qwe' port='5433'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * FROM home_books")
            data_search = self.cursor.fetchall()
            #self.tableWidget.setRowCount(0)
            #for row_number, row_data in enumerate(data_search):
            #    self.tableWidget.insertRow(row_number)
            #    for column_number, data in enumerate(row_data):
            #        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.connection.close()
        except:
            print("Cannot connect to to database")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1026, 734)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 140, 891, 271))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_load = QtWidgets.QPushButton(Form)
        self.btn_load.setGeometry(QtCore.QRect(540, 460, 111, 41))
        self.btn_load.setObjectName("btn_load")
        self.btn_load.clicked.connect()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_load.setText(_translate("Form", "LoadData"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #db_connect.DatabasConnector.database_connection.seach_data_in_table()
    sys.exit(app.exec_())

