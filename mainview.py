from PySide.QtGui import *
from PySide.QtCore import *


class MainView(QWidget):

    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.pnlLeft = QWidget()
        self.tbCategory = QDialogButtonBox(Qt.Horizontal)
        self.btnAddCategory = QPushButton(QIcon("add.png"), "")
        self.btnAddCategory.setFlat(True)
        self.btnEditCategory = QPushButton(QIcon("edit1.png"), "")
        self.btnEditCategory.setFlat(True)
        self.btnDelCategory = QPushButton(QIcon("del.png"), "")
        self.btnDelCategory.setFlat(True)
        self.btnRefreshCategory = QPushButton(QIcon("refresh.png"), "")
        self.btnRefreshCategory.setFlat(True)
        self.tbCategory.addButton(self.btnAddCategory, QDialogButtonBox.ActionRole)
        self.tbCategory.addButton(self.btnEditCategory, QDialogButtonBox.ActionRole)
        self.tbCategory.addButton(self.btnDelCategory, QDialogButtonBox.ActionRole)
        self.tbCategory.addButton(self.btnRefreshCategory, QDialogButtonBox.ActionRole)
        self.pnlLeftLayout = QGridLayout(self.pnlLeft)
        self.pnlLeftLayout.addWidget(self.tbCategory, 0, 0, Qt.AlignLeft)

        #self.pnlRight = QWidget()

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.pnlLeft)
        #self.layout.addWidget(self.lblRight, 0, 1)
        self.setLayout(self.layout)

"""
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(btnDialogs)
        self.setLayout(layout)
"""
