from flask import Blueprint, request

BP = Blueprint('message', __name__)


@BP.route('/send', methods=['POST'])
def send_message():
    return '<p>/api/message/send</p>'


@BP.route('/query', methods=['GET'])
def query_message():
    return '<p>/api/message/query</p>'
