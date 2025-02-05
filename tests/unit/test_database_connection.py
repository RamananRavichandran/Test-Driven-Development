import pytest

# Simulated database connection class
class Database:
    def connect(self):
        print("\n[SETUP] Connecting to database...")
        self.connection = "Connected"

    def disconnect(self):
        print("\n[TEARDOWN] Disconnecting from database...")
        self.connection = None

    def is_connected(self):
        return self.connection == "Connected"

# Pytest fixture for setup and teardown
@pytest.fixture
def db():
    db = Database()
    db.connect()  # Setup before test
    yield db      # Provide the fixture to the test
    db.disconnect()  # Teardown after test

# Test case using the fixture
def test_database_connection(db):
    print("[TEST] Checking database connection status...")
    assert db.is_connected()  # Test if the connection is active

