
from PyQt5 import QtWidgets, uic
import sys
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("untitled.ui")
window.btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())