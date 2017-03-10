"""
Диалог выбора базы данных для подключения
"""

from PySide.QtGui import (QDialog, QDialogButtonBox, QDesktopWidget, QIcon, QLabel,
                          QComboBox, QGridLayout, QVBoxLayout, QFont, QSizePolicy)
from PySide.QtCore import *


class DialogConnect(QDialog):

    def __init__(self, parent=None):
        super(DialogConnect, self).__init__(parent)

        # контролы
        lblChooseBase = QLabel("Выбор базы данных")
        # установим жирный шрифт
        boldFont = QFont()
        boldFont.setBold(True)
        lblChooseBase.setFont(boldFont)
        cbbChooseBase = QComboBox()
        # указываем политику изменения размера для ComboBox
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cbbChooseBase.sizePolicy().hasHeightForWidth())
        cbbChooseBase.setSizePolicy(sizePolicy)

        btnDialogs = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # layout
        grid = QGridLayout()
        grid.addWidget(lblChooseBase, 0, 0, Qt.AlignVCenter | Qt.AlignHCenter)
        grid.addWidget(cbbChooseBase, 1, 0)

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

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


