import ast
from flask import Blueprint, request, jsonify
from db.db_helper import pySql
from api.auth_config import auth

bp_info = Blueprint('get_info', __name__, url_prefix='/')


@bp_info.route('/login', methods=['POST'])
@auth.login_required
def login():
    return jsonify({"message": "authorization successful "}), 200


@bp_info.route('/api', methods=['POST'])
def get_user_data():
    cookies = request.headers.get('Authorization')
    if cookies is None:
        return jsonify({"message": "You are unauthorized to access this page"}), 300

    obj = pySql()
    json_obj = request.get_data()
    decode_data = json_obj.decode('utf-8')
    to_dict = ast.literal_eval(decode_data)

    test = [{
        'Key': 1,
        'Friend_name': 'TestName',
        'Last_online': '2018-03-01'},
        {'Key': 2,
         'Friend_name': 'TestName2',
         'Last_online': '2018-03-01'}]

    if 'FirstName' in to_dict.keys():
        query = 'select * from users where login = "' + to_dict.get('FirstName') + '"'
        res = obj.smart_query(query)
        result = jsonify([{"Login": ip[0],
                           "Password": ip[1],
                           "FirstName": ip[2],
                           "LastName": ip[3],
                           "Friends": test} for ip in res])
    else:
        result = 'There is no mandatory field: FirstName'
    return result
