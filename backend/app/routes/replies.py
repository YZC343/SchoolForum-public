from datetime import datetime

from cryptography.hazmat.asn1.asn1 import sequence
from flask import Blueprint, request, jsonify,session
from repositories.models import Reply,User
from repositories import db
from sqlalchemy import and_


BP = Blueprint('replies', __name__)


@BP.route('/publish', methods=['POST'])
def publish_reply():
    data = request.get_json()
    post_uuid = data.get('post_uuid')
    content = data.get('content')
    author =  session.get('username')
    if post_uuid != "" and content != "None" and author != "None":
        reply = Reply(content=content,post_uuid=post_uuid,created_time=datetime.now(),author_username=author)
        db.session.add(reply)
        db.session.commit()
        return jsonify({'status': 'publish_reply success'})
    else:
        return jsonify({'status': 'publish_reply error'}),500

@BP.route('/edit', methods=['POST'])
def edit_reply():
    username = session.get('username')
    data = request.get_json()
    uuid = data.get('uuid')
    sequence_no = data.get('sequence_no')
    content = data.get('content')
    reply = db.session.query(Reply).filter(Reply.post_uuid == uuid).filter(Reply.sequence_no == sequence_no).first()
    if reply != None and username == reply.author_username:
        reply.content = content
        db.session.commit()
        return jsonify({"status": "edited"})
    else:
        return jsonify({'status': 'pick_reply error'}), 500


@BP.route('/delete', methods=['POST'])
def delete_reply():
    username = session.get('username')
    user = User.query.filter_by(username=username).first()
    data = request.get_json()
    uuid = data.get('uuid')
    sequence_no = data.get('sequence_no')
    reply = db.session.query(Reply).filter(Reply.post_uuid == uuid).filter(Reply.sequence_no == sequence_no).first()
    if reply != None and user.is_super_admin == True:
        reply.is_deleted = True
        db.session.commit()
        return jsonify({"status": "deleted"})
    else:
        return jsonify({'status': 'pick_reply error'}), 500

@BP.route('/pick', methods=['POST'])
def pick_reply():
    data = request.get_json()
    uuid = data.get('uuid')
    sequence_no=data.get('sequence_no')
    reply = db.session.query(Reply).filter(Reply.post_uuid == uuid).filter(Reply.sequence_no==sequence_no).first()
    if reply != None:
        return jsonify(reply.to_dict())
    else:
        return jsonify({'status': 'pick_reply error'}),500

@BP.route('/list', methods=['POST'])
def reply():
    data = request.get_json()
    uuid = data.get('uuid')

    replies = Reply.query.filter_by(post_uuid=uuid).filter(Reply.is_deleted!=True).all()
    responsesDate = [reply.to_dict() for reply in replies]
    return jsonify(responsesDate)

@BP.route('/query_self', methods=['POST'])
def query_self():
    author = session.get('username')
    if author != "None":
        replies = Reply.query.filter_by(author_username=author).filter(Reply.is_deleted!=True).all()
        responsesDate = [reply.to_dict() for reply in replies]
        return jsonify(responsesDate)
    else:
        return jsonify({'status': 'username error'}),500
