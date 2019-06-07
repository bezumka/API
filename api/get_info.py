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

    if 'FirstName' in to_dict.keys():
        login_name = (to_dict.get('FirstName'))
        user_result = obj.smart_query_full('call user("' + login_name + '")')
    else:
        user_result = 'There is no mandatory field: FirstName'
    return user_result
