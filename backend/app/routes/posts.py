from flask import Blueprint, request,jsonify,session
from repositories.models.post import Post
from repositories.models.user import User
from repositories.database import db
from sqlalchemy import or_
import uuid
from datetime import datetime


BP = Blueprint('posts', __name__)


@BP.route('/publish', methods=['POST'])
def publish_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    board = data.get('board')
    author =  session.get('username')
    random_id = uuid.uuid4()
    if title != "" and content != "" and author != "":
        new_post = Post(uuid=random_id,title=title, content=content, board_name=board, author_username=author,created_time=datetime.now())
        db.session.add(new_post)
        db.session.commit()
        responsesDate = {"status":"published",
                         "title":title,
                         "content":content,
                         "board":board,
                         "author":author,
                         }
        return jsonify(responsesDate)
    else:
        return jsonify({"messages":"publish failed"})

@BP.route('/edit', methods=['POST'])
def edit_post():
    author = session.get('username')
    data = request.get_json()
    uuid = data.get('uuid')
    post = Post.query.filter_by(uuid=uuid).first()
    if author != post.author_username:
        return jsonify({"ststus":"edit failed"}),500
    else:
        title = data.get('title')
        content = data.get('content')
        post=Post.query.filter_by(uuid=uuid).first()
        post.title=title
        post.content=content
        db.session.commit()
        return jsonify({"status":"edited"})


@BP.route('/delete', methods=['POST'])
def delete_post():
    data = request.get_json()
    username = session.get('username')
    user = User.query.filter_by(username=username).first()
    uuid = data.get('uuid')
    post = Post.query.filter_by(uuid=uuid).first()
    if post!=None and user.is_super_admin == True:
        post.is_deleted = True
        db.session.commit()
        return jsonify({"status":"deleted"})
    else:
        return jsonify({"status":"delete failed"})

@BP.route('/pin', methods=['POST'])
def pin_post():
    return '<p>/api/posts/pin</p>'


@BP.route('/query', methods=['POST'])
def query_post():
    data = request.get_json()
    if data.get("keyword")!=None:
        keyword = data.get('keyword')
        posts = Post.query.filter(or_(Post.title.like(f'%{keyword}%'),Post.content.like(f'%{keyword}%'))).filter(Post.is_deleted!=True).all()
        posts_data = [post.to_dict() for post in posts]
        return jsonify(posts_data)
    else:
        board = data.get('board')
        posts = Post.query.filter_by(board_name=board).filter(Post.is_deleted!=True).all()
        posts_data = [post.to_dict() for post in posts]
        return jsonify(posts_data)

@BP.route('/query_self', methods=['POST'])
def query_self():
    author =  session.get('username')
    if author != None:
        posts = Post.query.filter(Post.author_username==author).filter(Post.is_deleted!=True).all()
        posts_data = [post.to_dict() for post in posts]
        return jsonify(posts_data)
    else:
        return jsonify({"status":"username error"}),500


@BP.route('/pick', methods=['POST'])
def pick_post():

    data = request.get_json()
    uuid = data.get('uuid')
    if uuid != None:
        post = Post.query.filter_by(uuid=uuid).first()
        return jsonify(post.to_dict())
    else:
        return jsonify({"message":"pick failed"}),500


@BP.route('/like', methods=['POST'])
def like_post():
    data = request.get_json()
    uuid = data.get('uuid')
    username = session.get('username')
    post = Post.query.filter_by(uuid=uuid).first()
    user = User.query.filter_by(username=username).first()
    if user in post.users_liking:
        post.users_liking.remove(user)
        db.session.commit()
        return jsonify({"status":"unliked"})
    else:
        post.users_liking.append(user)
        db.session.commit()
        return jsonify({"status":"liked"})


@BP.route('/collect', methods=['POST'])
def collect_post():
    return '<p>/api/posts/collect</p>'
