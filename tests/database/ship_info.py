from random import randint
import tests.database.query as Query
import tests.config.info_for_tables as TABLE
from framework.constants.db_method import DBMethod
from framework.database.database import Database

class ShipInfo():

    def __init__(self, DB_NAME):
        self.db = Database(DB_NAME=DB_NAME)
        
    def connect(self):
        self.db.connect()
        
    def close_connection(self):
        self.db.close_cursore()
        self.db.close_connection()

    def create_tables(self):
        self.db.execute(DBMethod.CREATE, Query.CREATE_ENGINES)
        self.db.execute(DBMethod.CREATE, Query.CREATE_HULLS)
        self.db.execute(DBMethod.CREATE, Query.CREATE_WEAPONS)
        self.db.execute(DBMethod.CREATE, Query.CREATE_SHIPS)
        
    def insert_random_info(self):
        for i in range(1,TABLE.WEAPONS_COUNT+1):
            values = []
            for l in range(0, len(TABLE.WEAPONS_VALUES)):
                if l == 0:
                    values.append(TABLE.WEAPONS_NAME + str(i))
                else: 
                    values.append(randint(1, TABLE.INT_PARAMS))
            sql = Query.INSERT_WEAPONS.format(
                ','.join(TABLE.WEAPONS_VALUES),
                ','.join(['?']*len(TABLE.WEAPONS_VALUES)))
            self.db.execute(DBMethod.INSERT, sql, values)
        
        for i in range(1,TABLE.HULLS_COUNT+1):
            values = []
            for l in range(0, len(TABLE.HULLS_VALUES)):
                if l == 0:
                    values.append(TABLE.HULLS_NAME + str(i))
                else: 
                    values.append(randint(1, TABLE.INT_PARAMS))
            sql = Query.INSERT_HULLS.format(
                ','.join(TABLE.HULLS_VALUES),
                ','.join(['?']*len(TABLE.HULLS_VALUES)))
            self.db.execute(DBMethod.INSERT, sql, values)
        
        for i in range(1,TABLE.ENGINES_COUNT+1):
            values = []
            for l in range(0, len(TABLE.ENGINES_VALUES)):
                if l == 0:
                    values.append(TABLE.ENGINES_NAME + str(i))
                else: 
                    values.append(randint(1, TABLE.INT_PARAMS))
            sql = Query.INSERT_ENGINES.format(
                ','.join(TABLE.ENGINES_VALUES),
                ','.join(['?']*len(TABLE.ENGINES_VALUES)))
            self.db.execute(DBMethod.INSERT, sql, values)
        
        for i in range(1,TABLE.SHIPS_COUNT+1):
            values = {
                'ship' : TABLE.SHIPS_NAME + str(i),
                'weapon' : TABLE.WEAPONS_NAME + str(randint(1,TABLE.WEAPONS_COUNT+1)),
                'hull' : TABLE.HULLS_NAME + str(randint(1,TABLE.HULLS_COUNT+1)),
                'engine' : TABLE.ENGINES_NAME + str(randint(1,TABLE.ENGINES_COUNT+1))
            }
            sql = Query.INSERT_SHIPS.format(
                ','.join(values.keys()),
                ','.join(['?']*len(values)))
            self.db.execute(DBMethod.INSERT, sql, tuple(values.values()))
