from flask import Flask, Blueprint, json, request, abort
from db.db_helper import pySql

bp_put = Blueprint('put_data', __name__, url_prefix='/')


@bp_put.route('/create_account', methods=['POST'])
def create_account():
    if not request.is_json:
        abort(400)

    return 'asd'
