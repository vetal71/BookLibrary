from PySide import QtCore, QtGui, QtSql


# описание графического интерфейса Главного окна
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
        iconAdd.addPixmap(QtGui.QPixmap(r"image\add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconEdit = QtGui.QIcon()
        iconEdit.addPixmap(QtGui.QPixmap(r"image\edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconDel = QtGui.QIcon()
        iconDel.addPixmap(QtGui.QPixmap(r"image\del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconRefresh = QtGui.QIcon()
        iconRefresh.addPixmap(QtGui.QPixmap(r"image\refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconRun = QtGui.QIcon()
        iconRun.addPixmap(QtGui.QPixmap(r"image\run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconSync = QtGui.QIcon()
        iconSync.addPixmap(QtGui.QPixmap(r"image\synclib.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iconExit = QtGui.QIcon()
        iconExit.addPixmap(QtGui.QPixmap(r"image\exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

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

        # правая панель
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

        # панель поиска
        self.frameFind = QtGui.QFrame(self.rightPanel)
        self.frameFind.setObjectName("frameFind")
        self.frameFind.setMinimumSize(0, 20)
        self.frameFind.setFrameShape(QtGui.QFrame.NoFrame)
        self.hlFrameFind = QtGui.QHBoxLayout(self.frameFind)
        self.hlFrameFind.setObjectName("hlFrameFind")
        self.edtFindString = QtGui.QLineEdit(self.frameFind)
        self.edtFindString.setObjectName("edtFindString")
        self.hlFrameFind.addWidget(self.edtFindString)
        self.btnFind = QtGui.QPushButton(self.frameFind)
        self.btnFind.setObjectName("btnFind")
        self.hlFrameFind.addWidget(self.btnFind)
        self.btnClear = QtGui.QPushButton(self.frameFind)
        self.btnClear.setObjectName("btnClear")
        self.hlFrameFind.addWidget(self.btnClear)
        self.vlRightPanel.addWidget(self.frameFind)

        # TableWidget
        self.tableWidget = QtGui.QTableView(self.rightPanel)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.setObjectName("tableWidget")
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

        self.lblDBInfo = QtGui.QLabel("Всего книг в библиотеке: {0}".format("?"))
        self.lblDBInfo.setMinimumWidth(350)
        self.statusbar.addPermanentWidget(self.lblDBInfo)
        self.lblDBName = QtGui.QLabel("База данных: {0}".format(self.__dbname))
        self.lblDBInfo.setMinimumWidth(250)
        self.statusbar.addPermanentWidget(self.lblDBName)
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actRefreshLib = QtGui.QAction(MainWindow)

        self.actRefreshLib.setIcon(iconSync)
        self.actRefreshLib.setObjectName("actRefreshLib")
        self.actExit = QtGui.QAction(MainWindow)
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

        # сигналы главного окна
        QtCore.QObject.connect(self.actExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actRefreshLib, QtCore.SIGNAL("triggered()"), self.refreshLibrary)

        # сигналы панели инструментов Категории
        QtCore.QObject.connect(self.btnAddCategory, QtCore.SIGNAL("clicked()"), self.addCategory)
        QtCore.QObject.connect(self.btnEditCategory, QtCore.SIGNAL("clicked()"), self.editCategory)
        QtCore.QObject.connect(self.btnDelCategory, QtCore.SIGNAL("clicked()"), self.delCategory)
        QtCore.QObject.connect(self.btnRefreshCategory, QtCore.SIGNAL("clicked()"), self.refreshCategory)

        # сигналы панели инструментов Книги
        QtCore.QObject.connect(self.btnAddBook, QtCore.SIGNAL("clicked()"), self.addBook)
        QtCore.QObject.connect(self.btnEditBook, QtCore.SIGNAL("clicked()"), self.editBook)
        QtCore.QObject.connect(self.btnDelBook, QtCore.SIGNAL("clicked()"), self.delBook)
        QtCore.QObject.connect(self.btnRefreshBook, QtCore.SIGNAL("clicked()"), self.refreshBook)
        QtCore.QObject.connect(self.btnView, QtCore.SIGNAL("clicked()"), self.viewBook)

        # поиск
        QtCore.QObject.connect(self.btnFind, QtCore.SIGNAL("clicked()"), self.findBook)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL("clicked()"), self.clearFindText)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        # self.tableWidget.setSortingEnabled(True)
        # self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Код", None, QtGui.QApplication.UnicodeUTF8))
        # self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        # self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Путь к файлу", None, QtGui.QApplication.UnicodeUTF8))
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

        self.btnFind.setText(QtGui.QApplication.translate("MainWindow", "Найти", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFind.setStatusTip(QtGui.QApplication.translate("MainWindow", "Поиск книг", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("MainWindow", "Очистить", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setStatusTip(QtGui.QApplication.translate("MainWindow", "Очистить поле для поиска", None, QtGui.QApplication.UnicodeUTF8))


