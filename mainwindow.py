"""
Класс главного окна
"""

from models.sqlquerymodel import *
from models.sqltreemodel import *
from PyQt5 import QtGui, QtSql, QtCore, QtWidgets
from mainwindow_ui import Ui_MainWindow


class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):

    # инициализация класса
    def __init__(self, dbname="", parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Библиотека книг")
        self.setWindowIcon(QtGui.QIcon(r"image\BookManager.ico"))
        self.lblDBName.setText("База данных: {0}".format(dbname))
        self.lblDBInfo.setText("Всего книг в библиотеке: {0}".format(self.getBookCount()))

        # self.loadCategory()
        self.loadBook()

        # сигналы главного меню
        self.actExit.triggered.connect(QtWidgets.qApp.quit)
        self.actRefreshLib.triggered.connect(self.refreshLibrary)
        # сигналы панели инструментов Категории
        self.btnAddCategory.clicked.connect(self.addCategory)
        self.btnEditCategory.clicked.connect(self.editCategory)
        self.btnDelCategory.clicked.connect(self.delCategory)
        self.btnRefreshCategory.clicked.connect(self.refreshCategory)
        # сигналы панели инструментов Книги
        self.btnAddBook.clicked.connect(self.addBook)
        self.btnEditBook.clicked.connect(self.editBook)
        self.btnDelBook.clicked.connect(self.delBook)
        self.btnRefreshBook.clicked.connect(self.refreshBook)
        self.btnView.clicked.connect(self.viewBook)
        # поиск
        self.btnFind.clicked.connect(self.findBook)
        self.btnClear.clicked.connect(self.clearFindText)

    """ ОБРАБОТЧИКИ """

    """ Обновление библиотеки """

    def refreshLibrary(self):
        print("Синхронизация файла базы данных {0}".format(self.__dbname))

    """ Обработчики событий нажатий кнопок панели инструментов Категории """

    def addCategory(self):
        """ Добавление категории """
        pass

    def editCategory(self):
        """ Редактирование категории """
        pass

    def delCategory(self):
        """ Удаление категории """
        pass

    def refreshCategory(self):
        """ Обновление списка категорий """
        pass

    """ Обработчики событий нажатий кнопок панели инструментов Книги """

    def addBook(self):
        """ Добавление книг """
        pass

    def editBook(self):
        """ Редактирование книг """
        pass

    def delBook(self):
        """ Удаление книг """
        pass

    def refreshBook(self):
        """ Обновление списка книг """
        pass

    def viewBook(self):
        """ Просмотр книги """
        pass

    def findBook(self):
        """ Поиск книги """
        pass

    def clearFindText(self):
        self.edtFindString.clear()
        self.edtFindString.setFocus()

    def loadCategory(self):
        categoryTree = self.treeWidget
        # Модель
        query = QtSql.QSqlQuery("select * from Categories")
        results = []
        header = ["ID", "CategoryName", "Parent_Id"]
        query.first()
        while query.next():
            record = [query.value(index) for index in range(len(header))]
            results.append(record)
        model = TreeModel(results)
        categoryTree.setModel(model)

    def loadBook(self):
        header_str = ['Код', 'Наименование', 'Путь к файлу', 'ID категории']
        bookView = self.tableWidget
        # Модель
        model = CustomSqlModel()
        model.setQuery("select Id, BookName, BookLink from Books")
        # меняем наименование столбцов
        for i in range(len(header_str)):
            model.setHeaderData(i, QtCore.Qt.Horizontal, header_str[i])
        bookView.setModel(model)
        bookView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        bookView.setColumnWidth(0, 60)
        bookView.setColumnWidth(1, 450)

    def getBookCount(self):
        query = QtSql.QSqlQuery("select count(*) as cnt from Books")
        cnt = 0
        while query.next():
            cnt = query.value(0)
        return cnt
