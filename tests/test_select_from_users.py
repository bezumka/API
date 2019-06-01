import unittest
import pymysql
from db.db_helper import pySql
from db.config import db_list


class BasicTests(unittest.TestCase):
    connection = None

    def setUp(self):
        env = 'DEV'
        self.db = (pymysql.connect(host=db_list[env]['host'],
                                   user=db_list[env]['user'],
                                   password=db_list[env]['passwd'],
                                   database=db_list[env]['database']))

    def test_select_user_from_db(self):
        sting = ('admin', 'admin', 'Vasya', 'Pupkin')
        obj = pySql()
        result = obj.smart_query('select * from users where login = "admin"')
        self.assertEqual(result[0], sting, msg='User not found or has wrong data')

    def test_no_duplicates_in_db(self):
        obj = pySql()
        result = obj.smart_query('select * from users where login = "admin"')
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()