import hashlib
from flask_httpauth import HTTPBasicAuth
from db.db_helper import pySql

auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == hashlib.md5(password.encode('utf-8')).hexdigest()


def get_admin_cred():
    obj = pySql()
    query = obj.smart_query_full("select * from admin;")
    return query


USER_DATA = dict(get_admin_cred())
