import pytest
from framework.database.database import Database
from tests.database.ship_info import ShipInfo

@pytest.fixture(scope="session")
def connect_to_db():
    db = Database()
    db.connect()

    yield

    db.close_cursore()
    db.close_connection()
    
@pytest.fixture(scope="session")
def work_with_db():
    ship = ShipInfo()
    ship.create_tables()
