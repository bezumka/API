import ast

from flask import Blueprint, request, abort
from db.db_helper import pySql

bp_put = Blueprint('put_data', __name__, url_prefix='/')


@bp_put.route('/create_account', methods=['POST'])
def create_account():
    if not request.is_json:
        abort(400)

    obj = pySql()
    json_obj = request.get_data()
    decode_data = json_obj.decode('utf-8')
    to_dict = ast.literal_eval(decode_data)

    values = list(to_dict.values())
    table = 'users'
    columns = ['login', 'password', 'first_name', 'last_name']

    if all(x in columns for x in list(to_dict.keys())):
        results = obj.insert_data_to_db(table, columns, values)
    else:
        results = "There is no mandatory field(s): " + str(set(columns) - set(to_dict.keys()))

    return str(results)
