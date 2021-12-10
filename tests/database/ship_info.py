import tests.database.query as Query
from framework.constants.db_method import DBMethod
from framework.database.database import Database

class ShipInfo():

    def __init__(self):
        self.db = Database()

    def create_tables(self):
        self.db.execute(DBMethod.CREATE, Query.CREATE_ENGINES)
        self.db.execute(DBMethod.CREATE, Query.CREATE_HULLS)
        self.db.execute(DBMethod.CREATE, Query.CREATE_WEAPONS)
        self.db.execute(DBMethod.CREATE, Query.CREATE_SHIPS)