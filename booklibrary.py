"""
Проект: BookLibrary
Назначение: Библиотека книг
"""

from PySide.QtGui import (QApplication)
from dlgconnect import DialogConnect
from mainwindow import MainWindow

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    dlgConn = DialogConnect()
    dlgConn.show()

    #mainWindow = MainWindow()
    #mainWindow.show()
    sys.exit(app.exec_())
