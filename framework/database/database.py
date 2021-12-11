import sqlite3 as sql
from framework.utils.logger import Logger
from framework.constants.db_method import DBMethod

class Database():
    
    def __init__(self, DB_NAME):
        self.__db_name = DB_NAME
        self.__connection = None
        self.__cursor = None
    
    def connect(self):
        try:
            Logger.info('Подключение к базе данных ' + self.__db_name)
            self.__connection = sql.connect(self.__db_name)
            self.__cursor = self.__connection.cursor()
        except sql.Error as error:
            Logger.info("Ошибка при подключении к sqlite" + error)
            
    def close_connection(self):
        Logger.info('Отключение от базы данных ' + self.__db_name)
        self.__connection.close()
        
    def execute(self, method : DBMethod, query, params = None):
        Logger.info('Применяю метод :' + method.name)
        try:
            if (method == DBMethod.CREATE or method == DBMethod.UPDATE):
                self.__cursor.execute(query)
            else:
                self.__cursor.execute(query, params)
            if (method == DBMethod.INSERT or
                    method == DBMethod.DELETE or method==DBMethod.CREATE):
                self.__connection.commit()
            if method == DBMethod.SELECT:
                self.elems = self.__cursor.fetchall()
        except sql.Error as error:
            Logger.warning(str(error))
            
    def close_cursore(self):
        self.__cursor.close()
