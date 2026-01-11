from flask import Blueprint, request,jsonify
from repositories.models.board import Board

BP = Blueprint('board', __name__)


@BP.route('/add', methods=['POST'])
def add_board():
    return '<p>/api/board/add</p>'



@BP.route('/list', methods=['GET'])
def list_board():
    boards = Board.query.all()
    responseData = [board.to_dict() for board in boards]
    data = [{'name':'板块1','content':'板块1内容'},{'name':'板块2','content':'板块2内容'},{'name':'板块3','content':'板块3内容'},{'name':'板块4','content':'板块4内容'},{'name':'板块5','content':'板块5内容'}]
    return jsonify(responseData)
