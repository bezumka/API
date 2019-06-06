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
        # query = obj.smart_query("SELECT id, CONCAT_WS(', ' , GROUP_CONCAT(first_name),"
        #                         " GROUP_CONCAT(last_name)) AS all_friends from users where login IN "
        #                           "(select f.friend from users u "
        #                           "INNER JOIN friends f ON u.login = f.login WHERE f.login = %s group by first_name)", (to_dict.get('FirstName'),))

        user = obj.smart_query("select * from users where login = %s", (to_dict.get('FirstName'),))
        friends = obj.smart_query("select id, first_name, last_name from users where login in "
                                  "(select f.friend from users u "
                                  "INNER JOIN friends f ON u.login = f.login "
                                  "WHERE f.login = %s)", (to_dict.get('FirstName'),))
        friend_result = [{"FirstName": ip[0],
                          "LastName": ip[1]} for ip in friends]
        user_result = jsonify([{"Login": ip[0],
                                "Password": ip[1],
                                "FirstName": ip[2],
                                "LastName": ip[3],
                                "Friends": friend_result} for ip in user])
    else:
        user_result = 'There is no mandatory field: FirstName'
    return user_result
