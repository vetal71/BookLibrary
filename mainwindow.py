"""
Класс главного окна
"""

from PySide.QtGui import (QMainWindow, QIcon)
from PySide import QtSql, QtCore
from mainwindow_ui import Ui_MainWindow


class MainForm(QMainWindow):

    # инициализация класса
    def __init__(self, dbname="", parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_MainWindow(dbname)
        self.ui.setupUi(self)
        self.setWindowTitle("Библиотека книг")
        self.setWindowIcon(QIcon(r"image\BookManager.ico"))
        self.loadCategory()
        self.loadBook()

    def loadCategory(self):
        categoryTree = self.ui.treeWidget
        # Модель
        model = QtSql.QSqlTableModel()
        model.setTable("Categories")
        model.select()
        categoryTree.setModel(model)

    def loadBook(self):
        header_str = ['Код', 'Наименование', 'Путь к файлу', 'ID категории']
        bookView = self.ui.tableWidget
        # Модель
        model = QtSql.QSqlTableModel()
        model.setTable("Books")
        model.select()
        # меняем наименование столбцов
        for i in range(len(header_str)):
            model.setHeaderData(i, QtCore.Qt.Horizontal, header_str[i])
        bookView.setModel(model)
        bookView.hideColumn(3)
        bookView.setColumnWidth(1, 450)