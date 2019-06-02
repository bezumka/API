import json
import unittest
from launcher import app
from utils.objects import Utilities


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_create_new_user_without_all_fields(self):
        response = self.app.test_client().post(
            '/create_account',
            data=json.dumps({'login': 'Admin', 'password': 'Admin'}),
            content_type='application/json',
        )
        res = (response.data.decode("utf-8"))
        self.assertEqual(res, 'Column count does not match value count at row', msg='Wrong error message')

    def test_create_user_without_value(self):
        response = self.app.test_client().post(
            '/create_account',
            data=json.dumps({'login': '', 'password': 'Admin'}),
            content_type='application/json',
        )
        res = (response.data.decode("utf-8"))
        self.assertEqual(res, "['Error: Login can not be empty']", msg='Wrong error message')

    def test_create_user_with_spec_char_in_login(self):
        response = self.app.test_client().post(
            '/create_account',
            data=json.dumps({'login': 'Admin*', 'password': 'Admin'}),
            content_type='application/json',
        )
        res = (response.data.decode("utf-8"))
        self.assertEqual(res, "['Error: Login can not contains special characters']", msg='Wrong error message')

    def test_create_user_with_short_login(self):
        # Less 4 characters - by default: 4
        response = self.app.test_client().post(
            '/create_account',
            data=json.dumps({'login': Utilities.random_string(3), 'password': 'Admin'}),
            content_type='application/json',
        )
        res = (response.data.decode("utf-8"))
        self.assertEqual(res, "['Error: Login should be more 4 or less 15 characters']", msg='Wrong error message')

    def test_create_user_with_long_login(self):
        # More 15 characters - by default: 15
        response = self.app.test_client().post(
            '/create_account',
            data=json.dumps({'login': Utilities.random_string(16), 'password': 'Admin'}),
            content_type='application/json',
        )
        res = (response.data.decode("utf-8"))
        self.assertEqual(res, "['Error: Login should be more 4 or less 15 characters']", msg='Wrong error message')