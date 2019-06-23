# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 477)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 561, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 521, 341))
        self.tableView.setObjectName("tableView")
        self.btn2ShowFull = QtWidgets.QPushButton(self.tab)
        self.btn2ShowFull.setGeometry(QtCore.QRect(450, 380, 91, 31))
        self.btn2ShowFull.setObjectName("btn2ShowFull")
        self.btn1Search = QtWidgets.QPushButton(self.tab)
        self.btn1Search.setGeometry(QtCore.QRect(340, 380, 91, 31))
        self.btn1Search.setObjectName("btn1Search")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 380, 91, 41))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(240, 0, 81, 21))
        self.label_2.setObjectName("label_2")
        self.button1 = QtWidgets.QPushButton(self.tab_2)
        self.button1.setGeometry(QtCore.QRect(30, 20, 131, 61))
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.tab_2)
        self.button2.setGeometry(QtCore.QRect(30, 100, 131, 61))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.tab_2)
        self.button3.setGeometry(QtCore.QRect(30, 180, 131, 61))
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.tab_2)
        self.button4.setGeometry(QtCore.QRect(30, 270, 131, 51))
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.tab_2)
        self.button5.setGeometry(QtCore.QRect(450, 390, 75, 23))
        self.button5.setObjectName("button5")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn2ShowFull.setText(_translate("Form", "btn2ShowFull"))
        self.btn1Search.setText(_translate("Form", "btn1Search"))
        self.label.setText(_translate("Form", "Введите данные \n"
" для поиска"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.label_2.setText(_translate("Form", "Разработка"))
        self.button1.setText(_translate("Form", "Нажми меня"))
        self.button2.setText(_translate("Form", "Кнопка 2"))
        self.button3.setText(_translate("Form", "Добавить данные \n"
" в Базу Данных"))
        self.button4.setText(_translate("Form", "Select * From \n"
" Data Base"))
        self.button5.setText(_translate("Form", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))

