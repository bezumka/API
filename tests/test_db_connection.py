import unittest
import pymysql
from db.config import db_list


class BasicTests(unittest.TestCase):
    connection = None

    def setUp(self):
        env = 'DEV'
        self.db = (pymysql.connect(host=db_list[env]['host'],
                                   user=db_list[env]['user'],
                                   password=db_list[env]['passwd'],
                                   database=db_list[env]['database']))

    def test_is_connected(self):
        self.assertIsNotNone(self.db.cursor())


if __name__ == "__main__":
    unittest.main()
