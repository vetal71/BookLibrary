"""
Класс главного окна
"""

from PySide.QtGui import (QMainWindow, QLabel, QIcon)


class MainWindow(QMainWindow):
    # конструктор класса
    def __init__(self, parent=None):
        # вызов родительского конструктора
        super(MainWindow, self).__init__(parent)
        # главное меню
        self.сreateMenu()
        # панель инструментов
        self.сreateToolbar()
        # статус строка
        self.createStatusBar()

        self.setWindowTitle("Библиотека книг")
        self.setWindowIcon(QIcon("BookManager.ico"))
        self.showMaximized()

    def сreateMenu(self):
        pass

    def сreateToolbar(self):
        pass

    def createStatusBar(self):
        lblHintPane = QLabel("Это статус строка для отображения подсказок")
        lblHintPane.setMinimumWidth(400)
        self.statusBar().addWidget(lblHintPane)

        lblDBStatusPane = QLabel("База данных:")
        lblDBStatusPane.setMinimumWidth(300)
        self.statusBar().addWidget(lblDBStatusPane)
