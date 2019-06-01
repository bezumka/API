import ast
from flask import Blueprint, json, request, abort
from db.db_helper import pySql

bp_info = Blueprint('get_info', __name__, url_prefix='/')


@bp_info.route('/api', methods=['POST'])
def get_user_data():
    if not request.is_json:
        abort(400)

    obj = pySql()
    json_obj = request.get_data()
    decode_data = json_obj.decode('utf-8')
    to_dict = ast.literal_eval(decode_data)

    if 'FirstName' in to_dict.keys():
        query = 'select * from users where login = "' + to_dict.get('FirstName') + '"'
        res = obj.smart_query(query)
        result = json.dumps([{"Login": ip[0],
                              "Password": ip[1],
                              "First Name": ip[2],
                              "Last Name": ip[3]} for ip in res])
    else:
        result = 'There is no mandatory field: FirstName'
    return result
