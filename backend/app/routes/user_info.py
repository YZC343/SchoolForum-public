from flask import Blueprint, request

BP = Blueprint('user_info', __name__)


@BP.route('/pick', methods=['GET'])
def pick_user_info():
    return '<p>/api/user_info/pick</p>'


@BP.route('/modify', methods=['POST'])
def modify_user_info():
    return '<p>/api/user_info/modify</p>'
