from flask import Blueprint, request

BP = Blueprint('user', __name__)


@BP.route('/subscribe', methods=['POST'])
def subscribe_user():
    request.form['follower']
    request.form['followee']
    return (
        f'<p>subscribe with {request.form['follower']=} {request.form['followee']=}</p>'
    )


@BP.route('/ban', methods=['POST'])
def ban_user():
    request.form['username']
    return f'<p>ban with {request.form['username']=}</p>'
