import os
from PyQt5 import QtSql, QtCore, QtGui


class CustomSqlModel(QtSql.QSqlQueryModel):
    def data(self, index, role):
        value = super(CustomSqlModel, self).data(index, role)
        if value is not None and role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return '#%d' % value
            elif index.column() == 1:
                return value.upper()

        if role == QtCore.Qt.BackgroundColorRole:
            pathfile = index.sibling(index.row(), 2).data(2)
            if not os.path.exists(pathfile):
                return QtGui.QColor(QtCore.Qt.red)

        if role == QtCore.Qt.TextAlignmentRole and index.column() == 0:
            return QtCore.Qt.AlignCenter

        # задает цвет текста в столбце
        # if role == QtCore.Qt.TextColorRole and index.column() == 1:
        #     return QtGui.QColor(QtCore.Qt.blue)

        return value
