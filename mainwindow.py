"""
Класс главного окна
"""

from PySide.QtGui import (QMainWindow)
from mainwindow_ui import Ui_MainWindow


class MainForm(QMainWindow):

    def __init__(self, dbname="", parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_MainWindow(dbname)
        self.ui.setupUi(self)



