"""
Проект: BookLibrary
Назначение: Библиотека книг
"""

from PySide.QtGui import (QApplication)
from dlgconnect import DialogConnect
from mainwindow import MainForm

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    dlgConn = DialogConnect()
    if dlgConn.exec_():
        dbname = dlgConn.dbname
        mainWindow = MainForm(dbname)
        mainWindow.show()

    sys.exit(app.exec_())
