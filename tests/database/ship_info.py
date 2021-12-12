from random import randint
from framework.utils.logger import Logger
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
        #Weapons
        values = '('
        for i in range(1,TABLE.WEAPONS_COUNT+1):
            for l in range(0, len(TABLE.WEAPONS_VALUES)):
                if l == 0:
                    values = values + "'" + \
                        TABLE.WEAPONS_NAME + str(i) + "'"
                else: 
                    values = values + ',' + \
                        str((randint(1, TABLE.INT_PARAMS)))
            if i == TABLE.WEAPONS_COUNT:
                values = values + ')'
            else: 
                values = values + '),('
        sql = Query.INSERT_WEAPONS.format(
                ','.join(TABLE.WEAPONS_VALUES), values)
        self.db.execute(DBMethod.INSERT, sql)
        
        #Hulls
        values = '('
        for i in range(1,TABLE.HULLS_COUNT+1):
            for l in range(0, len(TABLE.HULLS_VALUES)):
                if l == 0:
                    values = values + "'" + \
                        TABLE.HULLS_NAME + str(i) + "'"
                else: 
                    values = values + ',' + \
                        str((randint(1, TABLE.INT_PARAMS)))
            if i == TABLE.HULLS_COUNT:
                values = values + ')'
            else: 
                values = values + '),('
        sql = Query.INSERT_HULLS.format(
                ','.join(TABLE.HULLS_VALUES), values)
        self.db.execute(DBMethod.INSERT, sql)
        
        #Engines
        values = '('
        for i in range(1,TABLE.ENGINES_COUNT+1):
            for l in range(0, len(TABLE.ENGINES_VALUES)):
                if l == 0:
                     values = values + "'" + \
                         TABLE.ENGINES_NAME + str(i) + "'"
                else: 
                    values = values + ',' + \
                        str((randint(1, TABLE.INT_PARAMS)))
            if i == TABLE.ENGINES_COUNT:
                values = values + ')'
            else: 
                values = values + '),('
        sql = Query.INSERT_ENGINES.format(
                ','.join(TABLE.ENGINES_VALUES), values)
        self.db.execute(DBMethod.INSERT, sql)
        
        #Shipes
        values = "("
        for i in range(1,TABLE.SHIPS_COUNT+1):
            values = values + "'" + TABLE.SHIPS_NAME + \
                str(i) + "'" + ','
            values = values + "'" + TABLE.WEAPONS_NAME + \
                str(randint(1,TABLE.WEAPONS_COUNT+1)) + "'" + ','
            values = values + "'" + TABLE.HULLS_NAME + \
                str(randint(1,TABLE.HULLS_COUNT+1)) + "'"  + ','
            values = values + "'" + TABLE.ENGINES_NAME + \
                str(randint(1,TABLE.ENGINES_COUNT+1)) + "'"
            if i == TABLE.SHIPS_COUNT:
                values = values + ')'
            else: 
                values = values + '),('
            sql = Query.INSERT_SHIPS.format(
                ','.join(TABLE.SHIPS_VALUES), values)
        self.db.execute(DBMethod.INSERT, sql)

    def change_ship_info(self):
        for i in range(1,TABLE.SHIPS_COUNT+1):
            rand_param = randint(1,len(TABLE.SHIPS_VALUES)-1)
            param = TABLE.SHIPS_VALUES[rand_param]
            if rand_param == 1:
                value = TABLE.WEAPONS_NAME + str(randint(1,TABLE.WEAPONS_COUNT+1))
            elif rand_param == 2:
                value = TABLE.HULLS_NAME + str(randint(1,TABLE.HULLS_COUNT+1))
            elif rand_param == 3:
                value = TABLE.ENGINES_NAME + str(randint(1,TABLE.ENGINES_COUNT+1))
            sql = Query.UPDATE_SHIPS.format(param, value, TABLE.SHIPS_NAME + str(i))
            self.db.execute(DBMethod.UPDATE, sql)
            
    def change_other_info(self):
        for i in range(1,TABLE.WEAPONS_COUNT+1):
            rand_param = randint(1, len(TABLE.WEAPONS_VALUES)-1)
            param = TABLE.WEAPONS_VALUES[rand_param]
            value = randint(1, TABLE.INT_PARAMS)
            sql = Query.UPDATE_WEAPONS.format(param, value, TABLE.WEAPONS_NAME + str(i))
            self.db.execute(DBMethod.UPDATE, sql)
            
        for i in range(1,TABLE.HULLS_COUNT+1):
            rand_param = randint(1, len(TABLE.HULLS_VALUES)-1)
            param = TABLE.HULLS_VALUES[rand_param]
            value = randint(1, TABLE.INT_PARAMS)
            sql = Query.UPDATE_HULLS.format(param, value, TABLE.HULLS_NAME + str(i))
            self.db.execute(DBMethod.UPDATE, sql)
            
        for i in range(1,TABLE.ENGINES_COUNT+1):
            rand_param = randint(1, len(TABLE.ENGINES_VALUES)-1)
            param = TABLE.ENGINES_VALUES[rand_param]
            value = randint(1, TABLE.INT_PARAMS)
            sql = Query.UPDATE_ENGINES.format(param, value, TABLE.ENGINES_NAME + str(i))
            self.db.execute(DBMethod.UPDATE, sql)

    def get_ship_info(self, param, index):
        sql = Query.SELECT_SHIP.format(param, TABLE.SHIPS_NAME + str(index))
        self.db.execute(DBMethod.SELECT, sql)
        return self.db.get_elems()
    
    def get_weapon_info(self, weapon):
        sql = Query.SELECT_WEAPON.format(weapon)
        self.db.execute(DBMethod.SELECT, sql)
        return self.db.get_elems()
    
    def get_engine_info(self, engine):
        sql = Query.SELECT_ENGINE.format(engine)
        self.db.execute(DBMethod.SELECT, sql)
        return self.db.get_elems()
    
    def get_hull_info(self, hull):
        sql = Query.SELECT_HULL.format(hull)
        self.db.execute(DBMethod.SELECT, sql)
        return self.db.get_elems()
