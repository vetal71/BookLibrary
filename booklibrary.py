"""
Проект: BookLibrary
Назначение: Библиотека книг
"""
from funcs import *
from PyQt5.QtWidgets import QApplication
from dlgconnect import DialogConnect
from mainwindow import MainForm
from connection_module import *


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    dlgConn = DialogConnect()
    if dlgConn.exec_():
        dbname = dlgConn.dbname

        # соединение c БД
        db = Database(dbname)
        if db.connectToDatabase():
            mainWindow = MainForm(dbname)
            mainWindow.show()
        else:
            msg = "Не удалось установить подключение к базе данных {0}".format(dbname)
            showError(msg)

    sys.exit(app.exec_())
