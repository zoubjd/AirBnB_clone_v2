#!/usr/bin/python3
# tests/test_mysql_storage.py

import unittest
import MySQLdb
from models.state import State
from models import storage
import os

class TestMySQLStorage(unittest.TestCase):

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_create_state(self):
        """Test that a new State record is added to the database"""

        # Connect to the test database
        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = db.cursor()

        # Get the initial count of states
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]

        # Create a new state
        new_state = State(name="California")
        new_state.save()

        # Get the new count of states
        cursor.execute("SELECT COUNT(*) FROM states")
        new_count = cursor.fetchone()[0]

        # Assert that the count has increased by 1
        self.assertEqual(new_count, initial_count + 1)

        # Clean up
        cursor.execute("DELETE FROM states WHERE name = 'California'")
        db.commit()
        cursor.close()
        db.close()

if __name__ == '__main__':
    unittest.main()

