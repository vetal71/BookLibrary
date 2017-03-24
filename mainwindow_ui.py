from PyQt5 import QtCore, QtSql
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# описание графического интерфейса Главного окна
class Ui_MainWindow(object):

    def __init__(self, dbname=""):
        self.__dbname = dbname

    def setupUi(self, MainWindow):
        # главное окно
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 702)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # TabWidget
        self.tabMain = QTabWidget(self.centralwidget)
        self.tabMain.setObjectName("tabMain")
        self.tabLibrary = QWidget()
        self.tabLibrary.setEnabled(True)

        # Вкладка "Библиотека"
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabLibrary.sizePolicy().hasHeightForWidth())
        self.tabLibrary.setSizePolicy(sizePolicy)
        self.tabLibrary.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabLibrary.setObjectName("tabLibrary")
        self.gridLayout = QGridLayout(self.tabLibrary)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pnlView = QWidget(self.tabLibrary)
        self.pnlView.setObjectName("pnlView")
        self.hlPanelView = QHBoxLayout(self.pnlView)
        self.hlPanelView.setSpacing(5)
        self.hlPanelView.setContentsMargins(0, 0, 0, 0)
        self.hlPanelView.setObjectName("hlPanelView")

        # Левая панель - Категории
        self.leftPanel = QFrame(self.pnlView)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.leftPanel.setMinimumSize(QtCore.QSize(400, 0))
        self.leftPanel.setBaseSize(QtCore.QSize(400, 0))
        self.leftPanel.setFrameShape(QFrame.Panel)
        self.leftPanel.setFrameShadow(QFrame.Raised)
        self.leftPanel.setObjectName("leftPanel")
        self.glLeftPanel = QGridLayout(self.leftPanel)
        self.glLeftPanel.setContentsMargins(5, 5, 5, 5)
        self.glLeftPanel.setObjectName("glLeftPanel")
        self.vlLeftPanel = QVBoxLayout()
        self.vlLeftPanel.setObjectName("vlLeftPanel")
        self.hlCategoryToolbar = QHBoxLayout()
        self.hlCategoryToolbar.setObjectName("hlCategoryToolbar")

        # иконки для кнопок
        iconAdd = QIcon()
        iconAdd.addPixmap(QPixmap(r"image\add.png"), QIcon.Normal, QIcon.Off)
        iconEdit = QIcon()
        iconEdit.addPixmap(QPixmap(r"image\edit.png"), QIcon.Normal, QIcon.Off)
        iconDel = QIcon()
        iconDel.addPixmap(QPixmap(r"image\del.png"), QIcon.Normal, QIcon.Off)
        iconRefresh = QIcon()
        iconRefresh.addPixmap(QPixmap(r"image\refresh.png"), QIcon.Normal, QIcon.Off)
        iconRun = QIcon()
        iconRun.addPixmap(QPixmap(r"image\run.png"), QIcon.Normal, QIcon.Off)
        iconSync = QIcon()
        iconSync.addPixmap(QPixmap(r"image\synclib.png"), QIcon.Normal, QIcon.Off)
        iconExit = QIcon()
        iconExit.addPixmap(QPixmap(r"image\exit.png"), QIcon.Normal, QIcon.Off)

        # панель инструментов Категории
        self.btnAddCategory = QPushButton(self.leftPanel)
        self.btnAddCategory.setText("")
        self.btnAddCategory.setIcon(iconAdd)
        self.btnAddCategory.setFlat(True)
        self.btnAddCategory.setObjectName("btnAddCategory")
        self.hlCategoryToolbar.addWidget(self.btnAddCategory)
        self.btnEditCategory = QPushButton(self.leftPanel)
        self.btnEditCategory.setText("")
        self.btnEditCategory.setIcon(iconEdit)
        self.btnEditCategory.setFlat(True)
        self.btnEditCategory.setObjectName("btnEditCategory")
        self.hlCategoryToolbar.addWidget(self.btnEditCategory)
        self.btnDelCategory = QPushButton(self.leftPanel)
        self.btnDelCategory.setText("")
        self.btnDelCategory.setIcon(iconDel)
        self.btnDelCategory.setFlat(True)
        self.btnDelCategory.setObjectName("btnDelCategory")
        self.hlCategoryToolbar.addWidget(self.btnDelCategory)
        self.btnRefreshCategory = QPushButton(self.leftPanel)
        self.btnRefreshCategory.setText("")
        self.btnRefreshCategory.setIcon(iconRefresh)
        self.btnRefreshCategory.setFlat(True)
        self.btnRefreshCategory.setObjectName("btnRefreshCategory")
        self.hlCategoryToolbar.addWidget(self.btnRefreshCategory)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hlCategoryToolbar.addItem(spacerItem)
        self.vlLeftPanel.addLayout(self.hlCategoryToolbar)
        self.treeWidget = QTreeView(self.leftPanel)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName("treeWidget")
        self.vlLeftPanel.addWidget(self.treeWidget)
        self.glLeftPanel.addLayout(self.vlLeftPanel, 0, 0, 1, 1)
        self.hlPanelView.addWidget(self.leftPanel)

        # правая панель
        self.rightPanel = QFrame(self.pnlView)
        self.rightPanel.setFrameShape(QFrame.Panel)
        self.rightPanel.setFrameShadow(QFrame.Raised)
        self.rightPanel.setObjectName("rightPanel")
        self.gridLayout_3 = QGridLayout(self.rightPanel)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vlRightPanel = QVBoxLayout()
        self.vlRightPanel.setObjectName("vlRightPanel")
        self.hlBookToolbar = QHBoxLayout()
        self.hlBookToolbar.setObjectName("hlBookToolbar")
        self.btnAddBook = QPushButton(self.rightPanel)
        self.btnAddBook.setText("")
        self.btnAddBook.setIcon(iconAdd)
        self.btnAddBook.setFlat(True)
        self.btnAddBook.setObjectName("btnAddBook")
        self.hlBookToolbar.addWidget(self.btnAddBook)
        self.btnEditBook = QPushButton(self.rightPanel)
        self.btnEditBook.setText("")
        self.btnEditBook.setIcon(iconEdit)
        self.btnEditBook.setFlat(True)
        self.btnEditBook.setObjectName("btnEditBook")
        self.hlBookToolbar.addWidget(self.btnEditBook)
        self.btnDelBook = QPushButton(self.rightPanel)
        self.btnDelBook.setText("")
        self.btnDelBook.setIcon(iconDel)
        self.btnDelBook.setFlat(True)
        self.btnDelBook.setObjectName("btnDelBook")
        self.hlBookToolbar.addWidget(self.btnDelBook)
        self.btnRefreshBook = QPushButton(self.rightPanel)
        self.btnRefreshBook.setText("")
        self.btnRefreshBook.setIcon(iconRefresh)
        self.btnRefreshBook.setFlat(True)
        self.btnRefreshBook.setObjectName("btnRefreshBook")
        self.hlBookToolbar.addWidget(self.btnRefreshBook)
        self.btnView = QPushButton(self.rightPanel)
        self.btnView.setText("")
        self.btnView.setIcon(iconRun)
        self.btnView.setFlat(True)
        self.btnView.setObjectName("btnView")
        self.hlBookToolbar.addWidget(self.btnView)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hlBookToolbar.addItem(spacerItem1)
        self.vlRightPanel.addLayout(self.hlBookToolbar)

        # панель поиска
        self.frameFind = QFrame(self.rightPanel)
        self.frameFind.setObjectName("frameFind")
        self.frameFind.setMinimumSize(0, 20)
        self.frameFind.setFrameShape(QFrame.NoFrame)
        self.hlFrameFind = QHBoxLayout(self.frameFind)
        self.hlFrameFind.setObjectName("hlFrameFind")
        self.edtFindString = QLineEdit(self.frameFind)
        self.edtFindString.setObjectName("edtFindString")
        self.hlFrameFind.addWidget(self.edtFindString)
        self.btnFind = QPushButton(self.frameFind)
        self.btnFind.setObjectName("btnFind")
        self.hlFrameFind.addWidget(self.btnFind)
        self.btnClear = QPushButton(self.frameFind)
        self.btnClear.setObjectName("btnClear")
        self.hlFrameFind.addWidget(self.btnClear)
        self.vlRightPanel.addWidget(self.frameFind)

        # TableWidget
        self.tableWidget = QTableView(self.rightPanel)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.setObjectName("tableWidget")
        self.vlRightPanel.addWidget(self.tableWidget)

        self.gridLayout_3.addLayout(self.vlRightPanel, 0, 0, 1, 1)
        self.hlPanelView.addWidget(self.rightPanel)
        self.gridLayout.addWidget(self.pnlView, 0, 0, 1, 1)
        self.tabMain.addTab(self.tabLibrary, "")
        self.tabSQLMon = QWidget()
        self.tabSQLMon.setObjectName("tabSQLMon")
        self.gridLayout_2 = QGridLayout(self.tabSQLMon)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.tabSQLMon)
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.tabMain.addTab(self.tabSQLMon, "")
        self.horizontalLayout.addWidget(self.tabMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.mainMenu = QMenuBar(MainWindow)
        self.mainMenu.setGeometry(QtCore.QRect(0, 0, 1019, 21))
        self.mainMenu.setObjectName("mainMenu")
        self.mnuFile = QMenu(self.mainMenu)
        self.mnuFile.setObjectName("mnuFile")
        MainWindow.setMenuBar(self.mainMenu)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.lblDBInfo = QLabel()
        self.lblDBInfo.setMinimumWidth(350)
        self.statusbar.addPermanentWidget(self.lblDBInfo)
        self.lblDBName = QLabel()
        self.lblDBInfo.setMinimumWidth(250)
        self.statusbar.addPermanentWidget(self.lblDBName)
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actRefreshLib = QAction(MainWindow)

        self.actRefreshLib.setIcon(iconSync)
        self.actRefreshLib.setObjectName("actRefreshLib")
        self.actExit = QAction(MainWindow)
        self.actExit.setIcon(iconExit)
        self.actExit.setObjectName("actExit")
        self.mnuFile.addAction(self.actRefreshLib)
        self.mnuFile.addSeparator()
        self.mnuFile.addAction(self.actExit)
        self.mainMenu.addAction(self.mnuFile.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actRefreshLib)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actExit)

        self.retranslateUi(MainWindow)
        self.tabMain.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnFind.setText(_translate("MainWindow", "Найти"))
        self.btnClear.setText(_translate("MainWindow", "Очистить"))
        self.tableWidget.setSortingEnabled(True)
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabLibrary), _translate("MainWindow", "Библиотека"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabSQLMon), _translate("MainWindow", "SQL мониторинг"))
        self.mnuFile.setTitle(_translate("MainWindow", "&Файл"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actRefreshLib.setText(_translate("MainWindow", "Обновление библиотеки"))
        self.actRefreshLib.setStatusTip(_translate("MainWindow", "Сканирование каталога книг и обновление библиотеки"))
        self.actRefreshLib.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actExit.setText(_translate("MainWindow", "&Выход"))
        self.actExit.setStatusTip(_translate("MainWindow", "Выход из приложения"))
        self.actExit.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        
        self.btnAddCategory.setStatusTip(_translate("MainWindow", "Добавление новой категории"))
        self.btnEditCategory.setStatusTip(_translate("MainWindow", "Редактирование категории"))
        self.btnDelCategory.setStatusTip(_translate("MainWindow", "Удаление категории"))
        self.btnRefreshCategory.setStatusTip(_translate("MainWindow", "Обновление списка категорий"))

        self.btnAddBook.setStatusTip(_translate("MainWindow", "Добавление новой книги"))
        self.btnEditBook.setStatusTip(_translate("MainWindow", "Редактирование книги"))
        self.btnDelBook.setStatusTip(_translate("MainWindow", "Удаление книги"))
        self.btnRefreshBook.setStatusTip(_translate("MainWindow", "Обновление списка книг"))
        self.btnView.setStatusTip(_translate("MainWindow", "Просмотр книги"))
        self.btnView.setShortcut(_translate("MainWindow", "F5"))

        self.btnFind.setText(_translate("MainWindow", "Найти"))
        self.btnFind.setStatusTip(_translate("MainWindow", "Поиск книг"))
        self.btnClear.setText(_translate("MainWindow", "Очистить"))
        self.btnClear.setStatusTip(_translate("MainWindow", "Очистить поле для поиска"))

