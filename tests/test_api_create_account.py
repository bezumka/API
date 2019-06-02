import json
import unittest
from launcher import app


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
