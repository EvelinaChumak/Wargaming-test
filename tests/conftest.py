import pytest
import shutil
from framework.database.database import Database
from tests.database.ship_info import ShipInfo
from tests.config.db_connection import DB_NAME, COPY_DB_NAME

def pytest_configure():
    pytest.db = None
    pytest.copy_db = None

@pytest.fixture(scope="session")
def connect_and_fill_db():
    pytest.db = ShipInfo(DB_NAME=DB_NAME)
    pytest.db.connect()
    pytest.db.create_tables()
    pytest.db.insert_random_info()

    yield

    pytest.db.close_connection()
    

@pytest.fixture(scope="session")
def connect_and_change_copy_db():
    shutil.copy(DB_NAME, COPY_DB_NAME)
    pytest.copy_db = ShipInfo(DB_NAME=COPY_DB_NAME)
    pytest.copy_db.connect()
    pytest.copy_db.change_ship_info()

    yield

    pytest.copy_db.close_connection()
    