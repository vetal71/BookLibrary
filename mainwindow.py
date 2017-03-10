"""
Класс главного окна
"""

from PySide.QtGui import (QMainWindow, QLabel, QIcon, QAction, QTabWidget, QWidget)


class MainWindow(QMainWindow):
    # конструктор класса
    def __init__(self, dbname="", parent=None):
        # вызов родительского конструктора
        super(MainWindow, self).__init__(parent)

        self.__dbname = dbname

        # главное меню
        self.__mnuFile = self.сreateMenuItem("&Файл")
        self.__actRefreshLib = self.createAction("&Обновление библиотеки", self.__mnuFile,
                                                 self.refreshLibrary, "synclib.png")
        self.__mnuFile.addSeparator()
        self.__actExit = self.createAction("В&ыход", self.__mnuFile, self.close, "exit.png")

        # панель инструментов
        self.__tbrMain = self.сreateToolbar("")
        self.__tbrMain.addAction(self.__actRefreshLib)
        self.__tbrMain.addSeparator()
        self.__tbrMain.addAction(self.__actExit)

        # статус строка
        self.__sbMain = self.statusBar()
        self.__lblHintPain = QLabel()
        self.__lblHintPain.setMinimumWidth(400)
        self.__sbMain.addWidget(self.__lblHintPain)
        self.__lblDBStatusPane = QLabel("База данных: " + self.__dbname)
        self.__lblDBStatusPane.setMinimumWidth(300)
        self.statusBar().addWidget(self.__lblDBStatusPane)

        self.pgcMain = QTabWidget(self)
        self.setCentralWidget(self.pgcMain)
        # добавляем страницы
        self.pgcMain.addTab(QWidget(), "Библиотека книг")
        self.pgcMain.addTab(QWidget(), "Мониторинг")
        self.pgcMain.setCurrentIndex(0)

        self.setWindowTitle("Библиотека книг")
        self.setWindowIcon(QIcon("BookManager.ico"))
        self.showMaximized()


    def get_dbname(self):
        return self.__dbname

    def set_dbname(self, dbname):
        self.__dbname = dbname

    def сreateMenuItem(self, caption):
        # построение главного меню
        return self.menuBar().addMenu(caption)

    def сreateToolbar(self, caption):
        return self.addToolBar(caption)

    def createAction(self, text, menu, slot, icon=None):
        """
            хелпер для добавления подменю
        """
        if icon != None:
            action = QAction(QIcon(icon), text, self)
        else:
            action = QAction(text, self)
        menu.addAction(action)
        action.triggered.connect(slot)
        return action

    def refreshLibrary(self):
        print("Обновление библиотеки...")


