#include "qtdir/src/sql/drivers/psql/qsql_psql.cpp"
from PyQt5 import QtWidgets, QtSql
import sys

app = QtWidgets.QApplication(sys.argv)

con = QtSql.QSqlDatabase.addDatabase("QPSQL")
con.setHostName("localhost");
con.setPort(5432);
con.setDatabaseName("Own_library");
con.setUserName("postgres");
con.setPassword("123!qwe");
con.open();
print(con.isOpen())
con.close()
