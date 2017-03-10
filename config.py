import os
from configparser import ConfigParser


class ConfigParams(object):

    def __init__(self):
        # получаем текущий каталог
        curdir = os.getcwd()
        # создаем объект
        self.config = ConfigParser()
        self.filename = curdir + "\\conn.ini"
        self.config.read(self.filename)

    def getItems(self, section):
        return self.config.items(section)

"""
def readParams(self):

    items = config.items("Config")
    print(config.sections())
    db_driver, dbfile = items[1]
    print("Driver %s FileName %s" % (db_driver, dbfile))
    config.set("Config", "Version", "1.0")
    with open(filename, "w") as cf:
        config.write(cf)
"""