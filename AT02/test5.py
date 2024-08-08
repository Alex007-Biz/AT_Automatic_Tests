import pytest
from main5 import init_db,  add_user, get_user

@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()
