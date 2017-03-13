"""
Диалог выбора базы данных для подключения
"""
from PySide.QtGui import (QDialog, QDialogButtonBox, QDesktopWidget, QIcon, QLabel, QPushButton,
                          QComboBox, QGridLayout, QVBoxLayout, QFont, QSizePolicy)
from PySide.QtCore import *
from config import ConfigParams
from funcs import *


class DialogConnect(QDialog):

    def __init__(self, parent=None):
        super(DialogConnect, self).__init__(parent)
        # создаем интерфейс
        self.createUI()

    def createUI(self):
        """ Создание интерфейса """
        # контролы
        lblChooseBase = QLabel("Выбор базы данных")
        # установим жирный шрифт
        boldFont = QFont()
        boldFont.setBold(True)
        lblChooseBase.setFont(boldFont)
        self.cbbChooseBase = QComboBox()
        # заполняем комбобокс
        self.cbbChooseBase.addItems(self.getDatabaseList())
        # указываем политику изменения размера для ComboBox
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbbChooseBase.sizePolicy().hasHeightForWidth())
        self.cbbChooseBase.setSizePolicy(sizePolicy)

        # кнопки
        btnOK = QPushButton(self.tr("&OK"))
        btnOK.setDefault(True)
        btnCancel = QPushButton(self.tr("&Cancel"))
        btnDialogs = QDialogButtonBox(Qt.Horizontal)
        btnDialogs.addButton(btnOK, QDialogButtonBox.AcceptRole)
        btnDialogs.addButton(btnCancel, QDialogButtonBox.RejectRole)

        # layout
        grid = QGridLayout()
        grid.addWidget(lblChooseBase, 0, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        grid.addWidget(self.cbbChooseBase, 1, 0)

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(btnDialogs)
        self.setLayout(layout)

        # параметры окна
        self.setGeometry(0, 0, 450, 100)
        self.setWindowIcon(QIcon("BookManager.ico"))
        self.setWindowTitle("Соединение")
        # запрет показа кнопки "?" в заголовке окна
        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        # запрет изменения размера
        self.setFixedSize(self.size())
        self.center()

        # обработчики событий
        btnDialogs.accepted.connect(self.accept)
        btnDialogs.rejected.connect(self.reject)

    def center(self):
        """ Центрирование окна """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @staticmethod
    def getDatabaseList():
        config = ConfigParams()
        items = config.getItems("Database")
        dblist = []
        for i in range(len(items)):
            dbname, dbfile = items[i]
            dblist.append(dbname + "=" + dbfile)
        return dblist

    def getDBName(self):
        dbinfo = self.cbbChooseBase.currentText()
        return separateRight(dbinfo)

    @property
    def dbname(self):
        return self.getDBName()