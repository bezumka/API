import unittest
import pymysql
from db.db_helper import pySql
from db.config import db_list
from utils.objects import Utilities


class BasicTests(unittest.TestCase):
    connection = None

    def setUp(self):
        env = 'DEV'
        self.db = (pymysql.connect(host=db_list[env]['host'],
                                   user=db_list[env]['user'],
                                   password=db_list[env]['passwd'],
                                   database=db_list[env]['database']))

    def test_insert_user_to_db(self):
        obj = pySql()
        table = 'users'
        values = [Utilities.random_string(8)]
        columns = obj.get_column_names('select * from users')
        for i in range(len(columns) - 2):
            values.append('')

        result = obj.insert_data_to_db(table, columns[1:], values)
        self.assertEqual(result, 'Success Code: The HTTP 200 OK', msg='Wrong error message')


if __name__ == "__main__":
    unittest.main()
