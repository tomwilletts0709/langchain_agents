import os
import pytest 
from datetime import datetime



@pytest.fixture
def test_read_db(): 
    # Simulate a database connection and return a test database object
    class TestDB:
        def __init__(self):
            self.data = {"users": []}
        
        def add_user(self, user):
            self.data["users"].append(user)
    
    return TestDB()

@pytest.fixture(autouse=True)
def check_api_keys():
    if not os.environ.get("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set")