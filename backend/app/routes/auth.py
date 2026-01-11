from flask import Blueprint, request, jsonify,session
import datetime

from repositories.models.user import User
from repositories.database import db

BP = Blueprint('auth', __name__)


@BP.route('/register', methods=['POST'])
def register():
    #request.form['username']
    #request.form['pwd']
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': '用户名已存在'}), 409
    else :
        new_user = User(username=username,nickname=username,password=password,signature="这个人没有留下签名")

        # 保存到数据库
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"messages":"register success"})



@BP.route('/login', methods=['POST'])
def login():

    #request.form['username']
    #request.form['pwd']
    #return f'<p>login with {request.form['username']=} {request.form['pwd']=}</p>'

    data = request.get_json()
    username = data.get('username')
    password = data.get('pwd')

    user = User.query.filter_by(username=username).first()
    if user is not None and user.password == password:
        session.pop('username', None)
        session.pop('login_time', None)
        session['username'] = username
        session['login_time'] = str(datetime.datetime.now())
        return jsonify({
            'username': session.get('username'),
        })
    else:
        return jsonify({
            "status":"login failed",
        })

@BP.route('/info', methods=['POST'])
def info():
    author =  session.get('username')
    user = User.query.filter_by(username=author).first().to_dict()
    if user is None:
        return jsonify({"status":"name error"}),500
    else:
        return jsonify(user)





@BP.route('/unregister', methods=['POST'])
def unregister():
    request.form['username']
    return f'<p>unregister with {request.form['username']=}</p>'
