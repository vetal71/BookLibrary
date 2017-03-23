""" Модуль для соединения с базой данных """

import os
from PySide.QtCore import *
from PySide.QtSql import *

DATABASE_DRIVER = "QSQLITE"
DATABASE_HOSTNAME = "BookManager"


class Database(object):

    def __init__(self, dbname=""):
        self.__dbname = dbname
        # получаем текущий каталог
        self.__curdir = os.getcwd()
        self.__fullDbName = self.__curdir + "\\" + dbname
        self._db = QSqlDatabase()

    def connectToDatabase(self):
        """
        Перед подключением к базе данных производим проверку на её существование.
        В зависимости от результата производим открытие базы данных или её восстановление
        """
        if not (QFile(self.__fullDbName).exists()):
            return self.restoreDataBase()
        else:
            return self.openDataBase()

    def restoreDataBase(self):
        try:
            if self.openDataBase():
                if not self.createDataBase():
                    return False
                else:
                    return True
            else:
                print("Не удалось восстановить базу данных")
                return False
        except Exception as e:
            print(e.args)
            return False

    def openDataBase(self):
        """ База данных открывается по заданному пути и имени базы данных, если она существует """
        self._db = QSqlDatabase().addDatabase(DATABASE_DRIVER)
        self._db.setHostName(DATABASE_HOSTNAME)
        self._db.setDatabaseName(self.__fullDbName)
        if self._db.open():
            return True
        else:
            return False

    def createDataBase(self):
        query = QSqlQuery(self._db)
        scriptFile = QFile(self.__curdir + "\\script.sql")
        errorText = []
        if scriptFile.open(QIODevice.ReadOnly):
            scripts = QTextStream(scriptFile).readAll().split(';')
            for s in scripts:
                if not s.strip():
                    continue
                if not query.exec_(s):
                    errorText.append("Ошибка выполения запроса: {0} \n".format(query.lastError().text()))

            query.finish()
            if len(errorText) > 0:
                print(errorText)
                return False
            else:
                return True
        else:
            return False

    def closeDataBase(self):
        self._db.close()

