from email.policy import default

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(80),primary_key=True)
    password = db.Column(db.String(200), nullable=False)

'''
        def set_password(self, password):
        """设置密码（自动加密）"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """验证密码"""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """将用户对象转为字典"""
        return {
            'id': self.id,
            'username': self.username
        }
'''

class Post(db.Model):
    __tablename__ = 'posts'

    uuid = db.Column(db.String(36),primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    edit_count = db.Column(db.Integer, default=0)
    is_deleted = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    pin_weight = db.Column(db.Integer, default=0)
    author_name = db.Column(db.String(50), nullable=False)
    board_name = db.Column(db.String(100), nullable=False)
    referenced_post_uuid = db.Column(db.String(36))

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'title': self.title,
            'content': self.content,
            'edit_count': self.edit_count,
            'is_deleted': self.is_deleted,
            'create_time': self.create_time,
            'pin_weight': self.pin_weight,
            'author_name': self.author_name,
            'board_name': self.board_name,
            'referenced_post_uuid': self.referenced_post_uuid,
        }
