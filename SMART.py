import sys
from PySide6.QtWidgets import QApplication,QWidget
import sqlite3 as sq

app = QApplication(sys.argv)

win = QWidget()
win.resize(400,300)
win.setWindowTitle("SMART")

win.show()

sys.exit(app.exec())


