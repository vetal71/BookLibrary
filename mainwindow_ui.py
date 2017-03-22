from PySide import QtCore, QtGui

# конструктор класса
    # def __init__(self, dbname="", parent=None):
    #     # вызов родительского конструктора
    #     super(MainWindow, self).__init__(parent)
    #
    #     self.__dbname = dbname
    #
    #     # главное меню
    #     self.__mnuFile = self.сreateMenuItem("&Файл")
    #     self.__actRefreshLib = self.createAction("&Обновление библиотеки", self.__mnuFile,
    #                                              self.refreshLibrary, "synclib.png")
    #     self.__mnuFile.addSeparator()
    #     self.__actExit = self.createAction("В&ыход", self.__mnuFile, self.close, "exit.png")
    #
    #     # панель инструментов
    #     self.__tbrMain = self.сreateToolbar("")
    #     self.__tbrMain.addAction(self.__actRefreshLib)
    #     self.__tbrMain.addSeparator()
    #     self.__tbrMain.addAction(self.__actExit)
    #
    #     # статус строка
    #     self.__sbMain = self.statusBar()
    #     self.__lblHintPain = QLabel()
    #     self.__lblHintPain.setMinimumWidth(400)
    #     self.__sbMain.addWidget(self.__lblHintPain)
    #     self.__lblDBStatusPane = QLabel("База данных: " + self.__dbname)
    #     self.__lblDBStatusPane.setMinimumWidth(300)
    #     self.statusBar().addWidget(self.__lblDBStatusPane)
    #
    #     self.pgcMain = QTabWidget(self)
    #     self.setCentralWidget(self.pgcMain)
    #     # добавляем страницы
    #     tsView = Ui_Form()
    #         #MainView()
    #     self.pgcMain.addTab(tsView, "Библиотека книг")
    #     self.pgcMain.addTab(QWidget(), "Мониторинг")
    #     self.pgcMain.setCurrentIndex(0)
    #
    #     self.setWindowTitle("Библиотека книг")
    #     self.setWindowIcon(QIcon("BookManager.ico"))
    #     self.showMaximized()
    #
    # def get_dbname(self):
    #     return self.__dbname
    #
    # def set_dbname(self, dbname):
    #     self.__dbname = dbname
    #
    # def сreateMenuItem(self, caption):
    #     # построение главного меню
    #     return self.menuBar().addMenu(caption)
    #
    # def сreateToolbar(self, caption):
    #     return self.addToolBar(caption)
    #
    # def createAction(self, text, menu, slot, icon=None):
    #     """
    #         хелпер для добавления подменю
    #     """
    #     if icon != None:
    #         action = QAction(QIcon(icon), text, self)
    #     else:
    #         action = QAction(text, self)
    #     menu.addAction(action)
    #     action.triggered.connect(slot)
    #     return action
    #
    # def refreshLibrary(self):
    #     print("Обновление библиотеки...")


class Ui_MainWindow(object):

    def __init__(self, dbname=""):
        self.__dbname = dbname

    def setupUi(self, MainWindow):
        # главное окно
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 702)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # TabWidget
        self.tabMain = QtGui.QTabWidget(self.centralwidget)
        self.tabMain.setObjectName("tabMain")
        self.tabLibrary = QtGui.QWidget()
        self.tabLibrary.setEnabled(True)

        # Вкладка "Библиотека"
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabLibrary.sizePolicy().hasHeightForWidth())
        self.tabLibrary.setSizePolicy(sizePolicy)
        self.tabLibrary.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabLibrary.setObjectName("tabLibrary")
        self.gridLayout = QtGui.QGridLayout(self.tabLibrary)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pnlView = QtGui.QWidget(self.tabLibrary)
        self.pnlView.setObjectName("pnlView")
        self.hlPanelView = QtGui.QHBoxLayout(self.pnlView)
        self.hlPanelView.setSpacing(5)
        self.hlPanelView.setContentsMargins(0, 0, 0, 0)
        self.hlPanelView.setObjectName("hlPanelView")

        # Левая панель - Категории
        self.leftPanel = QtGui.QFrame(self.pnlView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.leftPanel.setMinimumSize(QtCore.QSize(400, 0))
        self.leftPanel.setBaseSize(QtCore.QSize(400, 0))
        self.leftPanel.setFrameShape(QtGui.QFrame.Panel)
        self.leftPanel.setFrameShadow(QtGui.QFrame.Raised)
        self.leftPanel.setObjectName("leftPanel")
        self.glLeftPanel = QtGui.QGridLayout(self.leftPanel)
        self.glLeftPanel.setContentsMargins(5, 5, 5, 5)
        self.glLeftPanel.setObjectName("glLeftPanel")
        self.vlLeftPanel = QtGui.QVBoxLayout()
        self.vlLeftPanel.setObjectName("vlLeftPanel")
        self.hlCategoryToolbar = QtGui.QHBoxLayout()
        self.hlCategoryToolbar.setObjectName("hlCategoryToolbar")

        # иконки для кнопок
        iconAdd = QtGui.QIcon()
        iconAdd.addPixmap(QtGui.QPixmap("add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconEdit = QtGui.QIcon()
        iconEdit.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconDel = QtGui.QIcon()
        iconDel.addPixmap(QtGui.QPixmap("del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconRefresh = QtGui.QIcon()
        iconRefresh.addPixmap(QtGui.QPixmap("refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconRun = QtGui.QIcon()
        iconRun.addPixmap(QtGui.QPixmap("run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # панель инструментов Категории
        self.btnAddCategory = QtGui.QPushButton(self.leftPanel)
        self.btnAddCategory.setText("")
        self.btnAddCategory.setIcon(iconAdd)
        self.btnAddCategory.setFlat(True)
        self.btnAddCategory.setObjectName("btnAddCategory")
        self.hlCategoryToolbar.addWidget(self.btnAddCategory)
        self.btnEditCategory = QtGui.QPushButton(self.leftPanel)
        self.btnEditCategory.setText("")
        self.btnEditCategory.setIcon(iconEdit)
        self.btnEditCategory.setFlat(True)
        self.btnEditCategory.setObjectName("btnEditCategory")
        self.hlCategoryToolbar.addWidget(self.btnEditCategory)
        self.btnDelCategory = QtGui.QPushButton(self.leftPanel)
        self.btnDelCategory.setText("")
        self.btnDelCategory.setIcon(iconDel)
        self.btnDelCategory.setFlat(True)
        self.btnDelCategory.setObjectName("btnDelCategory")
        self.hlCategoryToolbar.addWidget(self.btnDelCategory)
        self.btnRefreshCategory = QtGui.QPushButton(self.leftPanel)
        self.btnRefreshCategory.setText("")
        self.btnRefreshCategory.setIcon(iconRefresh)
        self.btnRefreshCategory.setFlat(True)
        self.btnRefreshCategory.setObjectName("btnRefreshCategory")
        self.hlCategoryToolbar.addWidget(self.btnRefreshCategory)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.hlCategoryToolbar.addItem(spacerItem)
        self.vlLeftPanel.addLayout(self.hlCategoryToolbar)
        self.treeWidget = QtGui.QTreeWidget(self.leftPanel)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(50)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.treeWidget.header().setStretchLastSection(True)
        self.vlLeftPanel.addWidget(self.treeWidget)
        self.glLeftPanel.addLayout(self.vlLeftPanel, 0, 0, 1, 1)
        self.hlPanelView.addWidget(self.leftPanel)
        self.rightPanel = QtGui.QFrame(self.pnlView)
        self.rightPanel.setFrameShape(QtGui.QFrame.Panel)
        self.rightPanel.setFrameShadow(QtGui.QFrame.Raised)
        self.rightPanel.setObjectName("rightPanel")
        self.gridLayout_3 = QtGui.QGridLayout(self.rightPanel)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.vlRightPanel = QtGui.QVBoxLayout()
        self.vlRightPanel.setObjectName("vlRightPanel")
        self.hlBookToolbar = QtGui.QHBoxLayout()
        self.hlBookToolbar.setObjectName("hlBookToolbar")
        self.btnAddBook = QtGui.QPushButton(self.rightPanel)
        self.btnAddBook.setText("")
        self.btnAddBook.setIcon(iconAdd)
        self.btnAddBook.setFlat(True)
        self.btnAddBook.setObjectName("btnAddBook")
        self.hlBookToolbar.addWidget(self.btnAddBook)
        self.btnEditBook = QtGui.QPushButton(self.rightPanel)
        self.btnEditBook.setText("")
        self.btnEditBook.setIcon(iconEdit)
        self.btnEditBook.setFlat(True)
        self.btnEditBook.setObjectName("btnEditBook")
        self.hlBookToolbar.addWidget(self.btnEditBook)
        self.btnDelBook = QtGui.QPushButton(self.rightPanel)
        self.btnDelBook.setText("")
        self.btnDelBook.setIcon(iconDel)
        self.btnDelBook.setFlat(True)
        self.btnDelBook.setObjectName("btnDelBook")
        self.hlBookToolbar.addWidget(self.btnDelBook)
        self.btnRefreshBook = QtGui.QPushButton(self.rightPanel)
        self.btnRefreshBook.setText("")
        self.btnRefreshBook.setIcon(iconRefresh)
        self.btnRefreshBook.setFlat(True)
        self.btnRefreshBook.setObjectName("btnRefreshBook")
        self.hlBookToolbar.addWidget(self.btnRefreshBook)
        self.btnView = QtGui.QPushButton(self.rightPanel)
        self.btnView.setText("")

        self.btnView.setIcon(iconRun)
        self.btnView.setFlat(True)
        self.btnView.setObjectName("btnView")
        self.hlBookToolbar.addWidget(self.btnView)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlBookToolbar.addItem(spacerItem1)
        self.vlRightPanel.addLayout(self.hlBookToolbar)
        self.tableWidget = QtGui.QTableWidget(self.rightPanel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.vlRightPanel.addWidget(self.tableWidget)
        self.gridLayout_3.addLayout(self.vlRightPanel, 0, 0, 1, 1)
        self.hlPanelView.addWidget(self.rightPanel)
        self.gridLayout.addWidget(self.pnlView, 0, 0, 1, 1)
        self.tabMain.addTab(self.tabLibrary, "")
        self.tabSQLMon = QtGui.QWidget()
        self.tabSQLMon.setObjectName("tabSQLMon")
        self.gridLayout_2 = QtGui.QGridLayout(self.tabSQLMon)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tabSQLMon)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.tabMain.addTab(self.tabSQLMon, "")
        self.horizontalLayout.addWidget(self.tabMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.mainMenu = QtGui.QMenuBar(MainWindow)
        self.mainMenu.setGeometry(QtCore.QRect(0, 0, 1019, 21))
        self.mainMenu.setObjectName("mainMenu")
        self.mnuFile = QtGui.QMenu(self.mainMenu)
        self.mnuFile.setObjectName("mnuFile")
        MainWindow.setMenuBar(self.mainMenu)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.lblDBInfo = QtGui.QLabel("Всего книг в библиотеке: {0}".format("100"))
        self.lblDBInfo.setMinimumWidth(350)
        self.statusbar.addWidget(self.lblDBInfo)
        self.lblDBName = QtGui.QLabel("База данных: {0}".format(self.__dbname))
        self.lblDBInfo.setMinimumWidth(250)
        self.statusbar.addWidget(self.lblDBName)

        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actRefreshLib = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("synclib.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRefreshLib.setIcon(icon5)
        self.actRefreshLib.setObjectName("actRefreshLib")
        self.actExit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actExit.setIcon(icon6)
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

        # сигналы главного окна
        QtCore.QObject.connect(self.actExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actRefreshLib, QtCore.SIGNAL("triggered()"), self.refreshLibrary)

        # сигналы панели инструментов Категории
        QtCore.QObject.connect(self.btnAddCategory, QtCore.SIGNAL("clicked()"), self.addCategory)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def refreshLibrary(self):
        print("Синхронизация файла базы данных {0}".format(self.__dbname))

    def addCategory(self):
        """ Добавление категории """
        print("Новая категория ...")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Код", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Всего", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).setText(1, QtGui.QApplication.translate("MainWindow", "Все книги", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Код", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Путь к файлу", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabLibrary), QtGui.QApplication.translate("MainWindow", "Библиотека", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabSQLMon), QtGui.QApplication.translate("MainWindow", "SQL мониторинг", None, QtGui.QApplication.UnicodeUTF8))
        self.mnuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&Файл", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actRefreshLib.setText(QtGui.QApplication.translate("MainWindow", "Обновление библиотеки", None, QtGui.QApplication.UnicodeUTF8))
        self.actRefreshLib.setStatusTip(QtGui.QApplication.translate("MainWindow", "Сканирование каталога книг и обновление библиотеки", None, QtGui.QApplication.UnicodeUTF8))
        self.actRefreshLib.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actExit.setText(QtGui.QApplication.translate("MainWindow", "&Выход", None, QtGui.QApplication.UnicodeUTF8))
        self.actExit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Выход из приложения", None, QtGui.QApplication.UnicodeUTF8))
        self.actExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F4", None, QtGui.QApplication.UnicodeUTF8))

        self.btnAddCategory.setStatusTip(QtGui.QApplication.translate("MainWindow", "Добавление новой категории", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditCategory.setStatusTip(QtGui.QApplication.translate("MainWindow", "Редактирование категории", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelCategory.setStatusTip(QtGui.QApplication.translate("MainWindow", "Удаление категории", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefreshCategory.setStatusTip(QtGui.QApplication.translate("MainWindow", "Обновление списка категорий", None, QtGui.QApplication.UnicodeUTF8))

        self.btnAddBook.setStatusTip(QtGui.QApplication.translate("MainWindow", "Добавление новой книги", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditBook.setStatusTip(QtGui.QApplication.translate("MainWindow", "Редактирование книги", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelBook.setStatusTip(QtGui.QApplication.translate("MainWindow", "Удаление книги", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefreshBook.setStatusTip(QtGui.QApplication.translate("MainWindow", "Обновление списка книг", None, QtGui.QApplication.UnicodeUTF8))
        self.btnView.setStatusTip(QtGui.QApplication.translate("MainWindow", "Просмотр книги", None, QtGui.QApplication.UnicodeUTF8))
        self.btnView.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))


